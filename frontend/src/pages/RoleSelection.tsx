import { useNavigate } from "react-router-dom";

export default function RoleSelection() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-indigo-900 to-slate-950 flex items-center justify-center p-8">

      <div className="max-w-5xl w-full">

        <h1 className="text-5xl font-bold text-white text-center mb-4">
          Choose Your Role
        </h1>

        <p className="text-center text-gray-400 text-lg mb-12">
          Continue as a Recruiter or Candidate
        </p>

        <div className="grid md:grid-cols-2 gap-8">

          {/* Recruiter Card */}

          <div
            onClick={() => navigate("/login?role=recruiter")}
            className="cursor-pointer bg-white/5 border border-white/10 rounded-3xl p-8 backdrop-blur-lg hover:scale-105 hover:border-purple-500 transition-all duration-300"
          >
            <div className="text-6xl mb-5">
              🏢
            </div>

            <h2 className="text-3xl font-bold text-white mb-3">
              Recruiter
            </h2>

            <p className="text-gray-400 mb-6">
              Upload job descriptions, analyze resumes,
              rank candidates and generate AI-powered hiring recommendations.
            </p>

            <button className="bg-purple-600 px-6 py-3 rounded-xl text-white font-semibold">
              Continue
            </button>
          </div>

          {/* Candidate Card */}

          <div
            onClick={() => navigate("/login?role=candidate")}
            className="cursor-pointer bg-white/5 border border-white/10 rounded-3xl p-8 backdrop-blur-lg hover:scale-105 hover:border-cyan-500 transition-all duration-300"
          >
            <div className="text-6xl mb-5">
              👨‍💼
            </div>

            <h2 className="text-3xl font-bold text-white mb-3">
              Candidate
            </h2>

            <p className="text-gray-400 mb-6">
              Upload your resume, view skill matching,
              identify missing skills and improve your ATS score.
            </p>

            <button className="bg-cyan-600 px-6 py-3 rounded-xl text-white font-semibold">
              Continue
            </button>
          </div>

        </div>

      </div>

    </div>
  );
}