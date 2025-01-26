"use client";

import React, { useState } from "react";

export default function Home() {
  const [text, setText] = useState("");
  const [category, setCategory] = useState("");
  const [loading, setLoading] = useState(false);

  const classifyText = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://localhost:4000/classify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error("ጽሑፉን መመደብ አልተሳካም");
      }

      const data: { class: keyof typeof categoryMap } = await response.json();
      const categoryMap = {
        "Local News": "የሀገር ውስጥ ዜና",
        Politics: "ፖለቲካ",
        Sports: "ስፖርት",
        Business: "ቢዝነስ",
        "International News": "ዓለም አቀፍ ዜና",
        Others: "ሌሎች",
      };

      const translatedCategory = categoryMap[data.class] || "ሌሎች";

      setCategory(translatedCategory);
    } catch (error) {
      console.error(error);
      setCategory("ጽሑፉን መመደብ ላይ ስህተት ተፈጥሯል");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-green-50 w-full h-screen overflow-hidden">
      <nav className="bg-green-600 w-full py-4 shadow-lg mb-4 transform -translate-y-1">
        <div className="flex justify-center items-center w-full h-full">
          <h1 className="text-white text-3xl font-semibold">የአማርኛ ጽሑፍ ምደባ</h1>
        </div>
      </nav>

      <main
        className="flex flex-col items-center justify-center h-full w-full"
        style={{ fontFamily: "Poppins, sans-serif" }}
      >
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          className="border border-green-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 rounded-lg p-4 mb-6 w-3/4 md:w-1/2 h-32 shadow-sm text-green-700"
          placeholder="ጽሑፉን ለመመደብ ያስገቡ"
        />
        <button
          onClick={classifyText}
          disabled={loading}
          className="bg-green-600 text-white py-2 px-6 rounded-lg hover:bg-green-700 disabled:bg-green-400 transition duration-300 shadow-lg"
        >
          {loading ? "በምደባ ላይ..." : "መድብ"}
        </button>
        {category && (
          <p className="mt-6 text-lg text-green-700">
            <strong>ምድብ:</strong> {category}
          </p>
        )}
      </main>
    </div>
  );
}
