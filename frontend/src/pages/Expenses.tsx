import { useEffect, useState } from "react";
import { api, Paginated } from "../api/client";
import { Expense } from "../api/types";
import PageHeader from "../components/PageHeader";

export default function Expenses() {
  const [list, setList] = useState<Expense[]>([]);
  useEffect(() => {
    api.get<Paginated<Expense>>("/expenses/").then((r) => setList(r.results)).catch(console.error);
  }, []);

  return (
    <>
      <PageHeader title="Expenses" />
      <div className="grid gap-2">
        {list.map((e) => (
          <div key={e.id} className="card p-4 flex justify-between">
            <div>
              <div className="font-medium">{e.category.replace("_", " ")}</div>
              <div className="text-sm text-slate-500">
                {e.date} · {e.vendor || "—"}
                {e.is_tax_deductible && (
                  <span className="badge bg-blue-100 text-blue-800 ml-2">tax-deductible</span>
                )}
              </div>
            </div>
            <div className="font-semibold">Rs {e.amount}</div>
          </div>
        ))}
        {list.length === 0 && (
          <div className="text-slate-500 text-sm text-center py-12">
            No expenses yet. Add via admin panel for now.
          </div>
        )}
      </div>
    </>
  );
}
