import type { ReactNode } from "react";

type AuthLayoutProps = {
  children: ReactNode;
};

export default function AuthLayout({ children }: AuthLayoutProps) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-950 via-black to-pink-950 flex items-center justify-center px-4">
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_left,rgba(168,85,247,0.15),transparent_40%),radial-gradient(circle_at_bottom_right,rgba(236,72,153,0.15),transparent_40%)]" />

      <div className="relative z-10 w-full max-w-md">
        {children}
      </div>
    </div>
  );
}