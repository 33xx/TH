import base64
exec(base64.b64decode(b'ZnJvbSB1c2VyYm90IGltcG9ydCBqbXRob24KCmZyb20gLi5jb3JlLm1hbmFnZXJzIGltcG9ydCBlZGl0X29yX3JlcGx5CmZyb20gLiBpbXBvcnQgKgoKcGx1Z2luX2NhdGVnb3J5ID0gInV0aWxzIgoKCkBqbXRob24uYXJfY21kKAogICAgcGF0dGVybj0i2YjYrNmHID8oLiopJCIsCiAgICBjb21tYW5kPSgi2YjYrNmHIiwgcGx1Z2luX2NhdGVnb3J5KSwKKQphc3luYyBkZWYgZ2Nhc3QoZXZlbnQpOgogICAgaWYgbm90IGV2ZW50Lm91dCBhbmQgbm90IGlzX2Z1bGxzdWRvKGV2ZW50LnNlbmRlcl9pZCk6CiAgICAgICAgcmV0dXJuIGF3YWl0IGVkaXRfb3JfcmVwbHkoZXZlbnQsICLZh9mA2LDYpyDYp9mE2KfZhdmA2LEg2YXZgtmA2YrYryDZhNmE2LPZgNmI2K/ZiCIpCiAgICB4eCA9IGV2ZW50LnBhdHRlcm5fbWF0Y2guZ3JvdXAoMSkKICAgIGlmIG5vdCB4eDoKICAgICAgICByZXR1cm4gZWRpdF9vcl9yZXBseShldmVudCwgIioqIOKZsO+4mdmK2KzZgNioINmI2LbZgNi5INmG2YDYtSDZhdi5INin2YTYp9mF2YDYsSDZhNmE2KrZiNis2YrZgNmHKioiKQogICAgdHQgPSBldmVudC50ZXh0CiAgICBtc2cgPSB0dFs2Ol0KICAgIGV2ZW50ID0gYXdhaXQgZWRpdF9vcl9yZXBseShldmVudCwgIioqIOKZsO+4mdmK2KrZgNmFINin2YTZgNiq2YjYrNmK2YDYqSDZhNmE2YDZhdis2YXZiNi52YDYp9iqINin2YbYqtmA2LjYsSDZgtmE2YrZhNinKioiKQogICAgZXIgPSAwCiAgICBkb25lID0gMAogICAgYXN5bmMgZm9yIHggaW4gYm90Lml0ZXJfZGlhbG9ncygpOgogICAgICAgIGlmIHguaXNfZ3JvdXA6CiAgICAgICAgICAgIGNoYXQgPSB4LmlkCiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIGRvbmUgKz0gMQogICAgICAgICAgICAgICAgYXdhaXQgYm90LnNlbmRfbWVzc2FnZShjaGF0LCBtc2cpCiAgICAgICAgICAgIGV4Y2VwdCBCYXNlRXhjZXB0aW9uOgogICAgICAgICAgICAgICAgZXIgKz0gMQogICAgYXdhaXQgZXZlbnQuZWRpdCgKICAgICAgICBmItiq2YDZhSDYqNmG2YDYrNmA2KfYrSDZgdmA2Yoge2RvbmV9INmF2YYg2KfZhNmA2K/Ysdiv2LTZgNin2KogLCDYrti32YDYoyDZgdmA2Yoge2VyfSDZhdmGINin2YTZgNiv2LHYr9i02YDYp9iqIgogICAgKQoKCkBqbXRob24uYXJfY21kKAogICAgcGF0dGVybj0i2K3ZiNmEID8oLiopJCIsCiAgICBjb21tYW5kPSgi2K3ZiNmEIiwgcGx1Z2luX2NhdGVnb3J5KSwKKQphc3luYyBkZWYgZ3VjYXN0KGV2ZW50KToKICAgIGlmIG5vdCBldmVudC5vdXQgYW5kIG5vdCBpc19mdWxsc3VkbyhldmVudC5zZW5kZXJfaWQpOgogICAgICAgIHJldHVybiBhd2FpdCBlZGl0X29yX3JlcGx5KGV2ZW50LCAi2YfZgNiw2Kcg2KfZhNin2YXZgNixINmF2YLZgNmK2K8g2YTZhNiz2YDZiNiv2YgiKQogICAgeHggPSBldmVudC5wYXR0ZXJuX21hdGNoLmdyb3VwKDEpCiAgICBpZiBub3QgeHg6CiAgICAgICAgcmV0dXJuIGVkaXRfb3JfcmVwbHkoZXZlbnQsICIqKiDimbDvuJnZitis2YDYqCDZiNi22YDYuSDZhtmA2LUg2YXYuSDYp9mE2KfZhdmA2LEg2YTZhNiq2YjYrNmK2YDZhyoqIikKICAgIHR0ID0gZXZlbnQudGV4dAogICAgbXNnID0gdHRbNzpdCiAgICBhd2FpdCBlZGl0X29yX3JlcGx5KGV2ZW50LCAiKiog4pmw77iZ2YrYqtmA2YUg2KfZhNmA2KrZiNis2YrZgNipINmE2YTYrtmA2KfYtSDYp9mG2KrZgNi42LEg2YLZhNmK2YTYpyoqIikKICAgIGVyID0gMAogICAgZG9uZSA9IDAKICAgIGFzeW5jIGZvciB4IGluIGJvdC5pdGVyX2RpYWxvZ3MoKToKICAgICAgICBpZiB4LmlzX3VzZXIgYW5kIG5vdCB4LmVudGl0eS5ib3Q6CiAgICAgICAgICAgIGNoYXQgPSB4LmlkCiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIGRvbmUgKz0gMQogICAgICAgICAgICAgICAgYXdhaXQgYm90LnNlbmRfbWVzc2FnZShjaGF0LCBtc2cpCiAgICAgICAgICAgIGV4Y2VwdCBCYXNlRXhjZXB0aW9uOgogICAgICAgICAgICAgICAgZXIgKz0gMQogICAgYXdhaXQgZXZlbnQuZWRpdCgKICAgICAgICBmItiq2YDZhSDYqNmG2YDYrNmA2KfYrSDZgdmA2Yoge2RvbmV9INmF2YYg2KfZhNmA2K/Ysdiv2LTZgNin2KogLCDYrti32YDYoyDZgdmA2Yoge2VyfSDZhdmGINin2YTZgNiv2LHYr9i02YDYp9iqIgogICAgKQo='))
