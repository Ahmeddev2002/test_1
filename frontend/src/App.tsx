import { Route, Routes } from "react-router-dom";
import Layout from "./components/Layout";
import Dashboard from "./pages/Dashboard";
import Properties from "./pages/Properties";
import PropertyDetail from "./pages/PropertyDetail";
import Tenants from "./pages/Tenants";
import TenantDetail from "./pages/TenantDetail";
import Leases from "./pages/Leases";
import Rent from "./pages/Rent";
import Expenses from "./pages/Expenses";
import Taxes from "./pages/Taxes";

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route index element={<Dashboard />} />
        <Route path="properties" element={<Properties />} />
        <Route path="properties/:id" element={<PropertyDetail />} />
        <Route path="tenants" element={<Tenants />} />
        <Route path="tenants/:id" element={<TenantDetail />} />
        <Route path="leases" element={<Leases />} />
        <Route path="rent" element={<Rent />} />
        <Route path="expenses" element={<Expenses />} />
        <Route path="taxes" element={<Taxes />} />
      </Route>
    </Routes>
  );
}
