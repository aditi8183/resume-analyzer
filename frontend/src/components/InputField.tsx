type Props = {
  type: string;
  placeholder: string;
};

export default function InputField({
  type,
  placeholder,
}: Props) {
  return (
    <input
      type={type}
      placeholder={placeholder}
      className="
        w-full
        p-4
        rounded-xl
        bg-white/5
        border
        border-white/10
        text-white
        placeholder-gray-400
        focus:outline-none
        focus:border-purple-500
      "
    />
  );
}