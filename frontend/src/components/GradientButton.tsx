type Props = {
  text: string;
  onClick?: () => void;
  type?: "button" | "submit";
};

export default function GradientButton({
  text,
  onClick,
  type = "button",
}: Props) {
  return (
    <button
      type={type}
      onClick={onClick}
      className="
        w-full
        p-4
        rounded-xl
        bg-gradient-to-r
        from-purple-600
        to-pink-600
        text-white
        font-semibold
        hover:scale-[1.02]
        hover:shadow-lg
        hover:shadow-pink-500/20
        transition-all
      "
    >
      {text}
    </button>
  );
}