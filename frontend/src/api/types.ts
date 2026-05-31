// Mirrors the Django REST serializers. Keep in sync when models change.

export type PropertyType = "house" | "apartment" | "plot";
export type AreaUnit = "marla" | "kanal" | "sq_ft" | "sq_yd";
export type PropertyStatus = "rented" | "vacant" | "under_construction" | "for_sale";

export interface Property {
  id: number;
  name: string;
  address: string;
  property_type: PropertyType;
  area_value: string | null;
  area_unit: AreaUnit;
  status: PropertyStatus;
  notes: string;
  photos: PropertyPhoto[];
  documents: PropertyDocument[];
  created_at: string;
  updated_at: string;
}

export interface PropertyPhoto {
  id: number;
  property: number;
  image: string;
  taken_on: string;
  category: "pre_tenant" | "current" | "damage" | "other";
  caption: string;
}

export interface PropertyDocument {
  id: number;
  property: number;
  title: string;
  doc_type: "registry" | "tax_receipt" | "utility" | "other";
  file: string;
  issued_on: string | null;
  notes: string;
}

export interface Tenant {
  id: number;
  name: string;
  cnic: string;
  phone: string;
  emergency_contact_name: string;
  emergency_contact_phone: string;
  photo: string | null;
  notes: string;
  documents: TenantDocument[];
}

export interface TenantDocument {
  id: number;
  tenant: number;
  title: string;
  doc_type: "cnic" | "lease" | "reference" | "other";
  file: string;
  notes: string;
}

export interface Lease {
  id: number;
  property: number;
  tenant: number;
  property_name: string;
  tenant_name: string;
  start_date: string;
  end_date: string | null;
  monthly_rent: string;
  security_deposit: string;
  annual_escalation_pct: string;
  rent_due_day: number;
  is_active: boolean;
  notes: string;
}

export interface RentInvoice {
  id: number;
  lease: number;
  period_start: string;
  period_end: string;
  due_date: string;
  amount_due: string;
  amount_paid: string;
  outstanding: string;
  is_paid: boolean;
  notes: string;
}

export interface Expense {
  id: number;
  property: number | null;
  date: string;
  category: string;
  amount: string;
  vendor: string;
  description: string;
  is_tax_deductible: boolean;
}

export interface TaxYearSummary {
  tax_year: number;
  period: { start: string; end: string };
  rent_collected: string;
  withholding_tax_credit: string;
  deductible_expenses: string;
  all_expenses: string;
  net_taxable_rental_income: string;
}
