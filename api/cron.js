export default async function handler(req, res) {
  try {
    const target = "https://remsmmprovider.kesug.com/cronjobs/order.php";
    const response = await fetch(target, {
      headers: {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
      }
    });

    const body = await response.text();
    return res.status(200).send(body);
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
}
