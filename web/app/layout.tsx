import "./styles.css";
import { headers } from "next/headers";
export const metadata = { title: "REC" };
export default function RootLayout({ children }: { children: React.ReactNode }) {
  const h = headers();
  const brand  = h.get("x-rec-brand")  ?? "default";
  const scheme = h.get("x-rec-scheme") ?? "auto";
  return (
    <html lang="en" data-brand={brand} data-color-scheme={scheme === "auto" ? "light" : scheme}>
      <head><meta name="color-scheme" content="light dark" /></head>
      <body>{children}</body>
    </html>
  );
}
