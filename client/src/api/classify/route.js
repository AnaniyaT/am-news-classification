export async function POST(req) {
  try {
    const { text } = await req.json();

    const categoryMap = {
      "Local News": "የሀገር ውስጥ ዜና",
      Politics: "ፖለቲካ",
      Sports: "ስፖርት",
      Business: "ቢዝነስ",
      "International News": "ዓለም አቀፍ ዜና",
      Others: "ሌሎች",
    };

    const translatedCategory = categoryMap[data.class] || "ሌሎች";

    return new Response(JSON.stringify({ class: translatedCategory }), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    });
  } catch (error) {
    return new Response(JSON.stringify({ error: "ጽሑፉን መመደብ ላይ ስህተት ተፈጥሯል" }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }
}
