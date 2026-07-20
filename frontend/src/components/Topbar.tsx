import { Bell, Search } from "lucide-react";

export default function Topbar() {
  return (
    <div className="flex justify-between items-center mb-8">
      <h2 className="text-3xl font-bold text-white">
        Recruiter Dashboard
      </h2>

      <div className="flex items-center gap-4">
        <div className="flex items-center gap-2 bg-white/5 px-4 py-2 rounded-xl">
          <Search size={18} />
          <input
            placeholder="Search candidates..."
            className="bg-transparent outline-none text-white"
          />
        </div>

        <Bell className="text-white" />
      </div>
    </div>
  );
}