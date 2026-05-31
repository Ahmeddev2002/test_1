import { useEffect, useState } from "react";
import { api, Paginated } from "../api/client";
import { Property, Tenant, Lease, TaxYearSummary } from "../api/types";
import PageHeader from "../components/PageHeader";

export default function Dashboard() {
  const [props, setProps] = useState<Paginated<Property>>();
  const [tenants, setTenants] = useState<Paginated<Tenant>>();
  const [leases, setLeases] = useState<Paginated<Lease>>();
  const [tax, setTax] = useState<TaxYearSummary>();

  useEffect(() => {
    const currentTaxYear = (() => {
      const now = new Date();
      // Pakistani TY ends 30 June. TY 2025 = Jul 2024–Jun 2025.
      return now.getMonth() >= 6 ? now.getFullYear() + 1 : now.getFullYear();
    })();

    api.get<Paginated<Property>>("/properties/").then(setProps).catch(console.error);
    api.get<Paginated<Tenant>>("/tenants/").then(setTenants).catch(console.error);
    api.get<Paginated<Lease>>("/leases/?is_active=true").then(setLeases).catch(console.error);
    api
      .get<TaxYearSummary>(`/tax-years/${currentTaxYear}/`)
      .then(setTax)
      .catch(console.error);
  }, []);

  return (
    <>
      <PageHeader title="Dashboard" />
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3 md:gap-4">
        <Stat label="Properties" value={props?.count} />
        <Stat label="Tenants" value={tenants?.count} />
        <Stat label="Active leases" value={leases?.count} />
        <Stat
          label={tax ? `TY ${tax.tax_year} rent` : "TY rent"}
          value={tax ? formatRs(tax.rent_collected) : undefined}
        />
      </div>

      {tax && (
        <div className="card p-4 mt-6">
          <h3 className="font-semibold mb-2">
            Tax year {tax.tax_year} — {tax.period.start} to {tax.period.end}
          </h3>
          <dl className="grid grid-cols-2 gap-y-1 text-sm">
            <dt className="text-slate-500">Rent collected</dt>
            <dd className="text-right">{formatRs(tax.rent_collected)}</dd>
            <dt className="text-slate-500">Deductible expenses</dt>
            <dd className="text-right">{formatRs(tax.deductible_expenses)}</dd>
            <dt className="text-slate-500">WHT credit</dt>
            <dd className="text-right">{formatRs(tax.withholding_tax_credit)}</dd>
            <dt className="font-medium pt-2 border-t mt-2">Net taxable</dt>
            <dd className="text-right font-medium pt-2 border-t mt-2">
              {formatRs(tax.net_taxable_rental_income)}
            </dd>
          </dl>
        </div>
      )}
    </>
  );
}

function Stat({ label, value }: { label: string; value: string | number | undefined }) {
  return (
    <div className="card p-4">
      <div className="text-xs text-slate-500 uppercase tracking-wide">{label}</div>
      <div className="text-2xl font-semibold mt-1">{value ?? "…"}</div>
    </div>
  );
}

function formatRs(v: string | number) {
  const n = typeof v === "string" ? Number(v) : v;
  return `Rs ${n.toLocaleString("en-PK", { maximumFractionDigits: 0 })}`;
}
