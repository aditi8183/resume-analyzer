import { useNavigate } from "react-router-dom";
 
const pipelineSteps = [
  { icon: "📄", title: "Resume Upload" },
  { icon: "🧠", title: "Resume Parsing" },
  { icon: "🎯", title: "Skill Extraction" },
  { icon: "📊", title: "ATS Scoring" },
  { icon: "🤖", title: "Semantic Matching" },
  { icon: "🏆", title: "Candidate Ranking" },
  { icon: "✅", title: "Hiring Recommendation" },
];
 
export default function Home() {
  const navigate = useNavigate();
 
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-indigo-900 to-slate-950">
 
      {/* Navbar */}
      <nav className="flex justify-between items-center px-10 py-6">
        <h1 className="text-2xl font-bold text-white">
          Smart Hiring Assistant
        </h1>
 
        <button
          onClick={() => navigate("/login")}
          className="bg-purple-600 hover:bg-purple-700 px-5 py-2 rounded-xl text-white"
        >
          Login
        </button>
      </nav>
 
      {/* Hero */}
      <div className="max-w-6xl mx-auto px-10 py-24 text-center">
 
        <h1 className="text-6xl font-extrabold text-white leading-tight">
          AI Powered Smart Hiring Assistant
          <br />
          & Resume Analysis Engine
        </h1>
 
        <p className="mt-8 text-xl text-gray-300 max-w-3xl mx-auto">
          Analyze resumes, identify skill gaps, rank candidates,
          and accelerate hiring decisions using explainable AI.
        </p>
 
        <div className="mt-10 flex justify-center gap-4">
          <button
            onClick={() => navigate("/choose-role")}
            className="bg-purple-600 hover:bg-purple-700 px-8 py-4 rounded-xl text-white font-semibold"
          >
            Get Started
          </button>
 
          <button
            className="border border-white/20 px-8 py-4 rounded-xl text-white"
          >
            Learn More
          </button>
        
        </div>
 
      </div>
 
      {/* AI Pipeline */}
 
      <section className="max-w-7xl mx-auto px-10 pb-24">
 
        <h2 className="text-4xl font-bold text-center text-white mb-14">
          AI Hiring Pipeline
        </h2>
 
        <div className="flex flex-wrap justify-center items-center gap-3">
 
          {pipelineSteps.map((step, index) => (
            <div
              key={index}
              className="flex items-center"
            >
              <div
                className="
                  bg-white/10
                  backdrop-blur-lg
                  border border-white/20
                  rounded-2xl
                  w-44
                  h-32
                  flex
                  flex-col
                  items-center
                  justify-center
                  hover:scale-105
                  hover:border-purple-400
                  hover:shadow-[0_0_30px_rgba(168,85,247,0.4)]
                  transition-all
                  duration-300
                "
              >
                <div className="text-4xl mb-2">
                  {step.icon}
                </div>
 
                <div className="text-white text-center font-semibold px-2">
                  {step.title}
                </div>
              </div>
 
              {index !== pipelineSteps.length - 1 && (
                <div className="text-purple-400 text-3xl px-2">
                  →
                </div>
              )}
            </div>
          ))}
 
        </div>
 
      </section>
 
    </div>
  );
}
