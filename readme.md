# neuralmed tech test

---

- [basic diagrams draws](https://drive.google.com/file/d/1-OAQeDuk_atgffoqL7oCIq7wZ5JPxSdQ/view?usp=sharing)

---

> To build this project
>
> <details>
>  <summary>at linux/mac os < - Click to expand!!!</summary>
>  
>  ```
>    make docker_build
>  ```
> </details>

> <details>
>  <summary>at windows < - Click to expand!!!</summary>
>  
>  ```
>    docker-compose -f .docker/docker-compose.yml build --no-cache
>  ```
> </details>

---

> To run this project
>
> <details>
>  <summary>at linux/mac os < - Click to expand!!!</summary>
>  
>  ```
>    make docker_up
>  ```
> </details>

> <details>
>  <summary>at windows < - Click to expand!!!</summary>
>  
>  ```
>    docker-compose -f .docker/docker-compose.yml up
>  ```
> </details>

---

> To run tests from project
>
> <details>
>  <summary>at linux/mac os < - Click to expand!!!</summary>
>  
>  ```
>    make test
>  ```
> </details>

> <details>
>  <summary>at windows < - Click to expand!!!</summary>
>  
>  ```
>    ./pandora_box/scripts/coverage.sh
>  ```
> </details>

---

## To make a tunnel from PUB/SUB Push events
please go to [ngrok](https://ngrok.com/download)

Download file, install, set-up and after this run a command bellow, to open a tunnel.

```
    ./ngrok http 5000
```
Copy the url woth HTTPS protocol and paste in GCP pub/sub pannel to receive notifications when a new event is published at QUEUE