export function formatDate(date: string): string {
  const dateInstance = new Date(date);
  const [d, t] = dateInstance.toISOString().split("T");
  return `${d} ${t.substring(0, 5)}`;
}
