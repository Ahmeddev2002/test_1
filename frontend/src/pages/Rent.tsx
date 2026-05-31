import { useEffect, useState } from "react";
import { api, Paginated } from "../api/client";
import { RentInvoice } from "../api/types";
import PageHeader from "../components/PageHeader";

export default function Rent() {
  const [list, setList] = useState<RentInvoice[]>([]);
  useEffect(() => {
    api
      .get<Paginated<RentInvoice>>("/rent-invoices/")
      .then((r) => setList(r.results))
      .catch(console.error);
  }, []);

  return (
    <>
      <PageHeader title="Rent" />
      <div className="grid gap-2">
        {list.map((i) => (
          <div key={i.id} className="card p-4 flex justify-between items-start">
            <div>
              <div className="font-medium">
                {i.period_start} → {i.period_end}
              </div>
              <div className="text-sm text-slate-500">Due {i.due_date}</div>
            </div>
            <div className="text-right">
              <div className="font-semibold">Rs {i.amount_due}</div>
              <div className={`text-xs ${i.is_paid ? "text-green-600" : "text-red-600"}`}>
                {i.is_paid ? "Paid" : `Outstanding Rs ${i.outstanding}`}
              </div>
            </div>
          </div>
        ))}
        {list.length === 0 && (
          <div className="text-slate-500 text-sm text-center py-12">
            No invoices yet. Auto-generation of monthly invoices from active leases is on the roadmap.
          </div>
        )}
      </div>
    </>
  );
}
