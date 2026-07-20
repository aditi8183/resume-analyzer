import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import { useSearchParams } from "react-router-dom";
import AuthLayout from "../components/AuthLayout";

export default function Login() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();

  const selectedRole =
   searchParams.get("role") || "";  

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (
    e: React.FormEvent
  ) => {
    e.preventDefault();

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/auth/login",
        {
          method: "POST",
          headers: {
            "Content-Type":
              "application/json",
          },
          body: JSON.stringify({
            email,
            password,
          }),
        }
      );

      const data =
        await response.json();

      if (!response.ok) {
        alert(data.detail);
        return;
      }

      localStorage.setItem(
        "token",
        data.access_token
      );

      localStorage.setItem(
        "user",
        JSON.stringify(data)
      );

      if (
        selectedRole &&
        data.role !== selectedRole
      ) {
        alert(
          `This account is registered as ${data.role}`
        );
        return;
      }

      if (data.role === "recruiter") {
        navigate("/recruiter");
      } else {
        navigate("/candidate");
      }   
    } catch (err) {
      console.error(err);
      alert("Login failed");
    }
  };

  return (
    <AuthLayout>
      <div className="bg-white/5 backdrop-blur-md border border-white/10 rounded-3xl p-8 shadow-2xl">
        <h1 className="text-4xl font-bold text-white text-center">
          {selectedRole === "candidate"
             ? "Candidate Login"
             : selectedRole === "recruiter"
              ? "Recruiter Login"
              : "Login"}
        </h1>

        <p className="text-gray-400 text-center mt-3">
          Sign in to continue
        </p>

        <form
          onSubmit={handleLogin}
          className="mt-8 space-y-5"
        >
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
              setPassword(
                e.target.value
              )
            }
            className="w-full p-4 rounded-xl bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500"
          />

          <button
            type="submit"
            className="w-full py-4 rounded-xl bg-gradient-to-r from-purple-600 to-pink-600 text-white font-semibold hover:scale-105 transition"
          >
            Sign In
          </button>
        </form>

        <p className="text-center text-gray-400 mt-6">
          Don't have an account?{" "}
          <Link
            to={
              selectedRole
                ? `/register?role=${selectedRole}`
                : "/register"
            }
            className="text-purple-400 hover:text-purple-300"
          >
            Register
          </Link>
        </p>
      </div>
    </AuthLayout>
  );
}