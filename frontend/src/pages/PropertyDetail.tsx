import { FormEvent, useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import { Property } from "../api/types";
import PageHeader from "../components/PageHeader";

export default function PropertyDetail() {
  const { id } = useParams<{ id: string }>();
  const [p, setP] = useState<Property>();

  const load = () => api.get<Property>(`/properties/${id}/`).then(setP).catch(console.error);
  useEffect(() => {
    load();
  }, [id]);

  if (!p) return <div>Loading…</div>;

  const uploadPhoto = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const form = e.currentTarget;
    const fd = new FormData(form);
    fd.append("property", String(p.id));
    try {
      await api.upload("/property-photos/", fd);
      form.reset();
      load();
    } catch (err) {
      alert(String(err));
    }
  };

  return (
    <>
      <PageHeader
        title={p.name}
        action={
          <Link to="/properties" className="btn-secondary">
            ← Back
          </Link>
        }
      />

      <div className="card p-4 space-y-1 text-sm">
        <div><span className="text-slate-500">Address:</span> {p.address}</div>
        <div><span className="text-slate-500">Type:</span> {p.property_type}</div>
        <div>
          <span className="text-slate-500">Area:</span> {p.area_value ?? "—"} {p.area_unit}
        </div>
        <div><span className="text-slate-500">Status:</span> {p.status}</div>
      </div>

      <h3 className="font-semibold mt-6 mb-2">Photos ({p.photos.length})</h3>
      <form onSubmit={uploadPhoto} className="card p-4 space-y-3 mb-3">
        <div className="grid md:grid-cols-3 gap-3">
          <div>
            <label className="label">Image</label>
            <input type="file" name="image" accept="image/*" capture="environment" required className="input" />
          </div>
          <div>
            <label className="label">Taken on</label>
            <input type="date" name="taken_on" required className="input" />
          </div>
          <div>
            <label className="label">Category</label>
            <select name="category" className="input" defaultValue="current">
              <option value="pre_tenant">Pre-tenant condition</option>
              <option value="current">Current state</option>
              <option value="damage">Damage record</option>
              <option value="other">Other</option>
            </select>
          </div>
          <div className="md:col-span-3">
            <label className="label">Caption</label>
            <input name="caption" className="input" />
          </div>
        </div>
        <button className="btn-primary">Upload photo</button>
      </form>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
        {p.photos.map((ph) => (
          <a key={ph.id} href={ph.image} target="_blank" className="card overflow-hidden">
            <img src={ph.image} alt={ph.caption} className="w-full h-32 object-cover" />
            <div className="p-2 text-xs">
              <div className="text-slate-500">{ph.taken_on}</div>
              <div className="truncate">{ph.caption || ph.category}</div>
            </div>
          </a>
        ))}
      </div>

      <h3 className="font-semibold mt-6 mb-2">Documents ({p.documents.length})</h3>
      <div className="grid gap-2">
        {p.documents.map((d) => (
          <a key={d.id} href={d.file} target="_blank" className="card p-3 text-sm flex justify-between">
            <span>
              <span className="font-medium">{d.title}</span>{" "}
              <span className="text-slate-400">— {d.doc_type}</span>
            </span>
            <span className="text-slate-400">{d.issued_on ?? ""}</span>
          </a>
        ))}
        {p.documents.length === 0 && (
          <div className="text-slate-500 text-sm">
            No documents yet. Upload via the admin panel for now.
          </div>
        )}
      </div>
    </>
  );
}
