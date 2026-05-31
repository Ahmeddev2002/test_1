import { useEffect, useState } from "react";
import { api } from "../api/client";
import { TaxYearSummary } from "../api/types";
import PageHeader from "../components/PageHeader";

export default function Taxes() {
  const [year, setYear] = useState(() => {
    const now = new Date();
    return now.getMonth() >= 6 ? now.getFullYear() + 1 : now.getFullYear();
  });
  const [tax, setTax] = useState<TaxYearSummary>();

  useEffect(() => {
    setTax(undefined);
    api.get<TaxYearSummary>(`/tax-years/${year}/`).then(setTax).catch(console.error);
  }, [year]);

  return (
    <>
      <PageHeader
        title="Tax year summary"
        action={
          <select
            value={year}
            onChange={(e) => setYear(Number(e.target.value))}
            className="input w-auto"
          >
            {[year + 1, year, year - 1, year - 2].map((y) => (
              <option key={y} value={y}>
                TY {y}
              </option>
            ))}
          </select>
        }
      />
      {!tax ? (
        <div>Loading…</div>
      ) : (
        <div className="card p-4">
          <div className="text-sm text-slate-500 mb-3">
            {tax.period.start} to {tax.period.end} (Pakistani fiscal year)
          </div>
          <dl className="grid grid-cols-2 gap-y-2 text-sm">
            <dt className="text-slate-500">Rent collected</dt>
            <dd className="text-right">Rs {tax.rent_collected}</dd>
            <dt className="text-slate-500">Deductible expenses</dt>
            <dd className="text-right">Rs {tax.deductible_expenses}</dd>
            <dt className="text-slate-500">All expenses</dt>
            <dd className="text-right">Rs {tax.all_expenses}</dd>
            <dt className="text-slate-500">Withholding tax credit</dt>
            <dd className="text-right">Rs {tax.withholding_tax_credit}</dd>
            <dt className="font-semibold pt-2 border-t mt-2">Net taxable rental income</dt>
            <dd className="text-right font-semibold pt-2 border-t mt-2">
              Rs {tax.net_taxable_rental_income}
            </dd>
          </dl>
        </div>
      )}
    </>
  );
}
