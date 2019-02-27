import json
from http.server import BaseHTTPRequestHandler, HTTPServer

def sync(parent, children):
  # Compute status based on observed state.
  desired_status = {
    "currentPod": ""
  }

  if len(children["Pod.v1"]) > 0:
    desired_status['currentPod'] = list(children["Pod.v1"])[0]

  # Generate the desired child object(s).
  image = parent.get("spec", {}).get("image", "World")
  desired_pods = [
    {
      "apiVersion": "v1",
      "kind": "Pod",
      "metadata": {
        "name": parent["metadata"]["name"]+"-immortalpod",
        "namespace": parent["metadata"]["namespace"],
      },
      "spec": {
        "restartPolicy": "OnFailure",
        "containers": [
          {
            "name": "acontainer",
            "image": image,
          }
        ]
      }
    }
  ]

  return {"status": desired_status, "children": desired_pods}


class Controller(BaseHTTPRequestHandler):
  def do_POST(self):
    # Serve the sync() function as a JSON webhook.
    self.headers
    observed = json.loads(self.rfile.read(int(self.headers.get("content-length"))))
    desired = sync(observed["parent"], observed["children"])

    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(desired).encode())

if __name__ == "__main__":
  HTTPServer(("", 80), Controller).serve_forever()