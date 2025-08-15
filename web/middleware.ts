import { NextResponse } from "next/server"; import type { NextRequest } from "next/server";
export function middleware(req: NextRequest) {
  const url = req.nextUrl; const brandQuery = url.searchParams.get("brand");
  const brandCookie = req.cookies.get("rec_brand")?.value;
  const schemeCookie = req.cookies.get("rec_color_scheme")?.value;
  const brand = brandQuery || brandCookie || "default"; if (brandQuery) { url.searchParams.delete("brand"); }
  const scheme = schemeCookie || "auto"; const res = NextResponse.rewrite(url);
  res.headers.set("x-rec-brand", brand); res.headers.set("x-rec-scheme", scheme);
  res.cookies.set("rec_brand", brand, { path: "/", httpOnly: false, sameSite: "lax" });
  res.cookies.set("rec_color_scheme", scheme, { path: "/", httpOnly: false, sameSite: "lax" });
  return res;
}
export const config = { matcher: ["/((?!_next|api|static).*)"] };
