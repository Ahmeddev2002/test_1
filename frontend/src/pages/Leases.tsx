import { useEffect, useState } from "react";
import { api, Paginated } from "../api/client";
import { Lease } from "../api/types";
import PageHeader from "../components/PageHeader";

export default function Leases() {
  const [list, setList] = useState<Lease[]>([]);
  useEffect(() => {
    api.get<Paginated<Lease>>("/leases/").then((r) => setList(r.results)).catch(console.error);
  }, []);

  return (
    <>
      <PageHeader title="Leases" />
      <div className="grid gap-3">
        {list.map((l) => (
          <div key={l.id} className="card p-4">
            <div className="flex justify-between">
              <div className="font-semibold">
                {l.tenant_name} @ {l.property_name}
              </div>
              <span className={`badge ${l.is_active ? "bg-green-100 text-green-800" : "bg-slate-100"}`}>
                {l.is_active ? "Active" : "Ended"}
              </span>
            </div>
            <div className="text-sm text-slate-500 mt-1">
              {l.start_date} → {l.end_date ?? "open"} · Rs {l.monthly_rent}/mo · {l.annual_escalation_pct}% annual
            </div>
          </div>
        ))}
        {list.length === 0 && (
          <div className="text-slate-500 text-sm text-center py-12">
            No leases yet. Create one via the admin panel — full lease form is on the roadmap.
          </div>
        )}
      </div>
    </>
  );
}
