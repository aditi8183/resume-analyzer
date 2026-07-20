import UploadSection from "../components/UploadSection";
import { useNavigate } from "react-router-dom";

export default function RecruiterDashboard() {

  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");

    navigate("/login");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-indigo-900 to-slate-950 p-8">

      <div className="max-w-6xl mx-auto">

        <div className="flex justify-between items-center mb-8">

          <h1 className="text-4xl font-bold text-white">
            Recruiter Dashboard
          </h1>

          <button
            onClick={handleLogout}
            className="bg-red-600 hover:bg-red-700 px-5 py-3 rounded-xl text-white font-semibold"
          >
            Logout
          </button>

        </div>

        <UploadSection />

      </div>

    </div>
  );
}