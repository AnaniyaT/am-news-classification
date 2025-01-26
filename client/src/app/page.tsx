"use client";

import React, { useState } from "react";

const examples = [
  "ማንቸስተር ሲቲ በፕሪሚየር ሊጉ ያለፉትን አምስት ጨዋታዎች አልተሸነፈም። ቼልሲን ቅዳሜ ካስተናገደ በሏላ ከአርሰናል፣ ኒውካስል እና ሊቨርፑል ጋር በተከታታይ ይጫወታል። የሲቲን ትክክለኛ ደረጃ ልናውቅ ነው ብሏል የቢቢሲው እግር ኳስ ተንታኝ ክሪስ ሱተን። ቀላል ጨዋታዎችን ሲያከናወኑ ቢቆዩም ቀጣዮቹ ጨዋታዎች የውድድር ዓመቱን የሚወስኑ ናቸው። ወደ ሻምፒዮንስ ሊግ ጥሎ ማለፍ ካለፉ በቀጣይ ወር የሚኖራቸውን የጨዋታ መርሃ ግብር የበለጠ ከባድ ያደርገዋል ሲል አክሏል። ሱተን ማንቸስተር ሲቲ ከቼልሲ የሚያደርጉትን ጨምሮ ቀሪዎቹን የፕሪሚየር ሊጉን ጨዋታዎች እንደሚከተለው ገምቷል።",
  "ግጭት በሚካሄድባቸው የአማራ እና ኦሮሚያ ክልሎች ከፍርድ ውጭ የሚፈጸሙ ግድያዎች በአሳሳቢነት መቀጠላቸውን የኢትዮጵያ ሰብዓዊ መብቶች ኮሚሽን (ኢሰመኮ) አስታወቀ። ግድያዎቹ የተፈጸሙት በመንግሥት የጸጥታ ኃይሎች እንዲሁም በክልሎቹ በሚንቀሳቀሱ ታጣቂ ኃይሎች እንደሆነ ኢሰመኮ አርብ፣ ጥር 16/ 2017 ዓ.ም ያወጣው ሪፖርት አመልክቷል። የመንግሥት የጸጥታ ኃይሎች ለታጣቂዎቹ ድጋፍ ታደርጋላችሁ በሚል እንዲሁም ታጣቂዎቹ ገዢውን መንግሥት ትደግፋላችሁ በሚል እየተፈጸሙ ያሉ ግድያዎች አሳሳቢ እንደሆኑ ነው ኢሰመኮ በግጭት ዓውድ ውስጥ ባሉ አካካቢዎች የተፈጸሙ የሰብዓዊ መብት ጥሰቶችን ገምግሞ ጥር 16/ 2017 ዓ.ም ባወጣው የሩብ ዓመቱ ሪፖርት ያስታወቀው።",
  "ነዳጅ መንግሥት ከተመነው የመሸጫ ዋጋ በላይ ሲሸጡ የተገኙ ነጋዴዎች እስከ አምስት መቶ ሺህ ብር እንዲቀጡ የሚያደርግ አዋጅ በሕዝብ ተወካዮች ምክር ቤት ጸደቀ። በአዋጁ መሠረት ከመሸጫ ዋጋ በላይ በመሸጥ የሚፈጸም የመጀመሪያ ጥፋት ከሦስት መቶ ሃምሳ ሺህ እስከ አምስት መቶ ሺህ ብር ያስቀጣል። ድርጊቱ በተደጋጋሚ ከተፈጸመ የገንዘብ መቀጮው ላይ ከሦስት ዓመት እስከ አምስት ዓመት የሚደርስ የእስር ቅጣት እንደሚኖር አዋጁ ያትታል። ይህን ቅጣት የያዘው እና የነዳጅ ውጤቶችን የግብይት ሥርዓት ለመደንገግ የወጣው አዋጅ፤ ሐሙስ ጥር 1/2017 ዓ.ም. በተካሄደው የምክር ቤቱ ስብሰባ ላይ በአብላጫ ድምጽ ጸድቋል።",
  "ቭላድሚር ፑቲን የዩክሬንን ጦርነት ማስቆም ካልቻሉ በሩስያ ላይ ከፍተኛ ታሪፍ እና ተጨማሪ ማዕቀብ እንደሚጥሉ ዶናልድ ትራምፕ አስጠንቀቁ። ጦርነቱን አንዲቋጭ በማድረግ ለሩሲያና ለፕሬዚዳንቱን በጣም ትልቅ ጥቅም እያስገኙ መሆናቸውን ትሩዝ ሶሻል በተሰኘው ማህበራዊ ሚዲያቸው አስፍረዋል። ትራምፕ እአአ በየካቲት 2022 የተከፈተው የሩስያ ወረራ በአንድ ቀን ውስጥ እልባት እንደሚያገኙለት ቀደም ሲል ተናግረው ነበር። ሩሲያ በጉዳዩ ዙሪያ እስካሁን ምላሽ አልሰጠችም። ከፍተኛ ባለስልጣናት ከሰሞኑ ሞስኮ ከአዲሱ የአሜሪካ አስተዳደር ጋር ለመነጋገር ያላት ዕድል አነስተኛ መሆኑን ተናግረዋል።"
]

export default function Home() {
  const [text, setText] = useState("");
  const [category, setCategory] = useState("");
  const [loading, setLoading] = useState(false);

  const classifyText = async () => {
    setLoading(true);
    try {
      const response = await fetch(process.env.NEXT_PUBLIC_MODEL_URL ?? "http://localhost:4000/classify", {
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
    <div className="bg-green-50 w-full h-screen overflow-y-auto">
      <nav className="bg-green-600 w-full py-4 shadow-lg mb-4 transform -translate-y-1">
        <div className="flex justify-center items-center w-full h-full">
          <h1 className="text-white text-3xl font-semibold">የአማርኛ ጽሑፍ ምደባ</h1>
        </div>
      </nav>

      <main
        className="flex flex-col items-center justify-center max-h-screen w-full"
        style={{ fontFamily: "Poppins, sans-serif" }}
      >
        <p className="text-green-800">ምሳሌዎችን ለመጠቀም ጠቅ ያድርጉ</p>
        <div className="p-4 flex gap-4 text-green-800 mb-8 max-w-[80rem]">
          {
            examples.map((example) => {
              return (
                <div 
                  onClick={() => setText(example)}
                  key={example} 
                  className="border-green-500 border-2 rounded-xl line-clamp-5 cursor-pointer hover:bg-green-200"
                >
                  <p className="m-4 line-clamp-4">
                    {example}
                  </p> 
                </div>
              )
            })
          }
        </div>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          className="border border-green-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 rounded-lg p-4 mb-6 w-3/4 md:w-1/2 h-96 shadow-sm text-green-700"
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
