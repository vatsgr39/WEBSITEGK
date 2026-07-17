import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Gautam Kumar | Strategic Sourcing Leader",
  description: "Portfolio of Gautam Kumar, a strategic sourcing and commodity management professional creating measurable value across rail, automotive, and manufacturing.",
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
