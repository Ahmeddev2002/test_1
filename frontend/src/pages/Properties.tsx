import { FormEvent, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api, Paginated } from "../api/client";
import { Property } from "../api/types";
import PageHeader from "../components/PageHeader";

const STATUS_STYLES: Record<string, string> = {
  rented: "bg-green-100 text-green-800",
  vacant: "bg-yellow-100 text-yellow-800",
  under_construction: "bg-blue-100 text-blue-800",
  for_sale: "bg-purple-100 text-purple-800",
};

export default function Properties() {
  const [list, setList] = useState<Property[]>([]);
  const [showForm, setShowForm] = useState(false);

  const load = () =>
    api
      .get<Paginated<Property>>("/properties/")
      .then((r) => setList(r.results))
      .catch(console.error);

  useEffect(() => {
    load();
  }, []);

  return (
    <>
      <PageHeader
        title="Properties"
        action={
          <button className="btn-primary" onClick={() => setShowForm((s) => !s)}>
            {showForm ? "Cancel" : "+ Add"}
          </button>
        }
      />

      {showForm && (
        <NewPropertyForm
          onSaved={() => {
            setShowForm(false);
            load();
          }}
        />
      )}

      <div className="grid gap-3 mt-4">
        {list.map((p) => (
          <Link
            key={p.id}
            to={`/properties/${p.id}`}
            className="card p-4 hover:shadow-md transition flex justify-between items-start"
          >
            <div>
              <div className="font-semibold">{p.name}</div>
              <div className="text-sm text-slate-500">{p.address}</div>
              <div className="text-xs text-slate-400 mt-1">
                {p.property_type} · {p.area_value ?? "—"} {p.area_unit}
              </div>
            </div>
            <span className={`badge ${STATUS_STYLES[p.status] ?? "bg-slate-100"}`}>
              {p.status.replace("_", " ")}
            </span>
          </Link>
        ))}
        {list.length === 0 && (
          <div className="text-slate-500 text-sm text-center py-12">
            No properties yet. Click "+ Add" to create one.
          </div>
        )}
      </div>
    </>
  );
}

function NewPropertyForm({ onSaved }: { onSaved: () => void }) {
  const [saving, setSaving] = useState(false);
  const [err, setErr] = useState<string>();

  const submit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const fd = new FormData(e.currentTarget);
    const body = {
      name: fd.get("name"),
      address: fd.get("address"),
      property_type: fd.get("property_type"),
      area_value: fd.get("area_value") || null,
      area_unit: fd.get("area_unit"),
      status: fd.get("status"),
    };
    try {
      setSaving(true);
      await api.post("/properties/", body);
      onSaved();
    } catch (e) {
      setErr(String(e));
    } finally {
      setSaving(false);
    }
  };

  return (
    <form onSubmit={submit} className="card p-4 space-y-3">
      <div className="grid md:grid-cols-2 gap-3">
        <div>
          <label className="label">Name</label>
          <input name="name" required className="input" placeholder="House 12, Street 5" />
        </div>
        <div>
          <label className="label">Type</label>
          <select name="property_type" required className="input">
            <option value="house">House</option>
            <option value="apartment">Apartment</option>
            <option value="plot">Plot</option>
          </select>
        </div>
        <div className="md:col-span-2">
          <label className="label">Address</label>
          <textarea name="address" required className="input" rows={2} />
        </div>
        <div>
          <label className="label">Area</label>
          <input name="area_value" type="number" step="0.01" className="input" placeholder="10" />
        </div>
        <div>
          <label className="label">Unit</label>
          <select name="area_unit" className="input" defaultValue="marla">
            <option value="marla">Marla</option>
            <option value="kanal">Kanal</option>
            <option value="sq_ft">Sq Ft</option>
            <option value="sq_yd">Sq Yd</option>
          </select>
        </div>
        <div>
          <label className="label">Status</label>
          <select name="status" className="input" defaultValue="vacant">
            <option value="vacant">Vacant</option>
            <option value="rented">Rented</option>
            <option value="under_construction">Under construction</option>
            <option value="for_sale">For sale</option>
          </select>
        </div>
      </div>
      {err && <div className="text-sm text-red-600">{err}</div>}
      <button className="btn-primary" disabled={saving}>
        {saving ? "Saving…" : "Save property"}
      </button>
    </form>
  );
}
