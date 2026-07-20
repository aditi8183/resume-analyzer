import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import AuthLayout from "../components/AuthLayout";

export default function Register() {
  const navigate = useNavigate();

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("");

  const handleRegister = async (
    e: React.FormEvent
  ) => {
    e.preventDefault();

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/auth/register",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            name,
            email,
            password,
            role,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        alert(data.detail);
        return;
      }

      alert("Registration successful!");

      navigate("/login");
    } catch (err) {
      console.error(err);
      alert("Registration failed");
    }
  };

  return (
    <AuthLayout>
      <div className="bg-white/5 backdrop-blur-md border border-white/10 rounded-3xl p-8 shadow-2xl">
        <h1 className="text-4xl font-bold text-white text-center">
          Create Account
        </h1>

        <p className="text-gray-400 text-center mt-3">
          Join Smart Hiring Assistant
        </p>

        <form
          onSubmit={handleRegister}
          className="mt-8 space-y-4"
        >
          <input
            type="text"
            placeholder="Full Name"
            value={name}
            onChange={(e) =>
              setName(e.target.value)
            }
            className="w-full p-4 rounded-xl bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500"
          />

          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) =>
              setEmail(e.target.value)
            }
            className="w-full p-4 rounded-xl bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500"
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) =>
              setPassword(e.target.value)
            }
            className="w-full p-4 rounded-xl bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500"
          />

          <select
            value={role}
            onChange={(e) =>
              setRole(e.target.value)
            }
            className="w-full p-4 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-purple-500"
          >
            <option value="">
              Select Role
            </option>
            <option value="candidate">
              Candidate
            </option>
            <option value="recruiter">
              Recruiter
            </option>
          </select>

          <button
            type="submit"
            className="w-full py-4 rounded-xl bg-gradient-to-r from-purple-600 to-pink-600 text-white font-semibold hover:scale-105 transition"
          >
            Create Account
          </button>
        </form>

        <p className="text-center text-gray-400 mt-6">
          Already have an account?{" "}
          <Link
            to="/login"
            className="text-purple-400 hover:text-purple-300"
          >
            Sign In
          </Link>
        </p>
      </div>
    </AuthLayout>
  );
}