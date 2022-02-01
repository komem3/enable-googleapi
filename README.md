# Enable Google APIs

Script to enable googleapi.

## Usage

1. change and add service to want to enable.

```diff
@@ -28,4 +28,4 @@ if __name__ == "__main__":
     parser.add_argument("-p", "--project", type=int, help="target project number")
     args = parser.parse_args()

-    enable_service(args.project, ["artifactregistry", "vision"])
+    enable_service(args.project, ["artifactregistry", "appengine"])
```

2. run script

```shell
pipenv run init -p ${project_number}
```
