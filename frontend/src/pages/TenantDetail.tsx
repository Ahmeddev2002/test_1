import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import { Tenant } from "../api/types";
import PageHeader from "../components/PageHeader";

export default function TenantDetail() {
  const { id } = useParams<{ id: string }>();
  const [t, setT] = useState<Tenant>();
  useEffect(() => {
    api.get<Tenant>(`/tenants/${id}/`).then(setT).catch(console.error);
  }, [id]);

  if (!t) return <div>Loading…</div>;

  return (
    <>
      <PageHeader
        title={t.name}
        action={<Link to="/tenants" className="btn-secondary">← Back</Link>}
      />
      <div className="card p-4 space-y-1 text-sm">
        <div><span className="text-slate-500">CNIC:</span> {t.cnic}</div>
        <div><span className="text-slate-500">Phone:</span> {t.phone}</div>
        <div>
          <span className="text-slate-500">Emergency:</span>{" "}
          {t.emergency_contact_name} {t.emergency_contact_phone}
        </div>
      </div>
      <h3 className="font-semibold mt-6 mb-2">Documents ({t.documents.length})</h3>
      <div className="grid gap-2">
        {t.documents.map((d) => (
          <a key={d.id} href={d.file} target="_blank" className="card p-3 text-sm">
            <span className="font-medium">{d.title}</span>{" "}
            <span className="text-slate-400">— {d.doc_type}</span>
          </a>
        ))}
        {t.documents.length === 0 && (
          <div className="text-slate-500 text-sm">No documents. Upload via admin for now.</div>
        )}
      </div>
    </>
  );
}
