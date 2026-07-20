import {
  LayoutDashboard,
  Upload,
  Users,
  BarChart3,
  FileText,
} from "lucide-react";

const menu = [
  { icon: LayoutDashboard, label: "Dashboard" },
  { icon: Upload, label: "Upload" },
  { icon: Users, label: "Candidates" },
  { icon: BarChart3, label: "Analytics" },
  { icon: FileText, label: "Reports" },
];

export default function Sidebar() {
  return (
    <div className="w-64 bg-[#12091f] border-r border-white/10 min-h-screen p-6">
      <h1 className="text-2xl font-bold text-white mb-10">
        Smart ATS
      </h1>

      <div className="space-y-3">
        {menu.map((item) => (
          <button
            key={item.label}
            className="w-full flex items-center gap-3 p-3 rounded-xl text-gray-300 hover:bg-purple-600/20 hover:text-white transition"
          >
            <item.icon size={18} />
            {item.label}
          </button>
        ))}
      </div>
    </div>
  );
}