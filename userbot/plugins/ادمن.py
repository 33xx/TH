import base64

exec(
    base64.b64decode(
        b"ZnJvbSB0ZWxldGhvbi5lcnJvcnMgaW1wb3J0ICgKICAgIEJhZFJlcXVlc3RFcnJvciwKICAgIEltYWdlUHJvY2Vzc0ZhaWxlZEVycm9yLAogICAgUGhvdG9Dcm9wU2l6ZVNtYWxsRXJyb3IsCikKZnJvbSB0ZWxldGhvbi5lcnJvcnMucnBjZXJyb3JsaXN0IGltcG9ydCBVc2VySWRJbnZhbGlkRXJyb3IKZnJvbSB0ZWxldGhvbi50bC5mdW5jdGlvbnMuY2hhbm5lbHMgaW1wb3J0ICgKICAgIEVkaXRBZG1pblJlcXVlc3QsCiAgICBFZGl0QmFubmVkUmVxdWVzdCwKICAgIEVkaXRQaG90b1JlcXVlc3QsCikKZnJvbSB0ZWxldGhvbi50bC50eXBlcyBpbXBvcnQgKAogICAgQ2hhdEFkbWluUmlnaHRzLAogICAgQ2hhdEJhbm5lZFJpZ2h0cywKICAgIElucHV0Q2hhdFBob3RvRW1wdHksCiAgICBNZXNzYWdlTWVkaWFQaG90bywKKQoKZnJvbSB1c2VyYm90IGltcG9ydCBqbXRob24KCmZyb20gLi5jb3JlLmxvZ2dlciBpbXBvcnQgbG9nZ2luZwpmcm9tIC4uY29yZS5tYW5hZ2VycyBpbXBvcnQgZWRpdF9kZWxldGUsIGVkaXRfb3JfcmVwbHkKZnJvbSAuLmhlbHBlcnMudXRpbHMgaW1wb3J0IF9mb3JtYXQsIGdldF91c2VyX2Zyb21fZXZlbnQKZnJvbSAuLnNxbF9oZWxwZXIubXV0ZV9zcWwgaW1wb3J0IGlzX211dGVkCmZyb20gLiBpbXBvcnQgQk9UTE9HLCBCT1RMT0dfQ0hBVElECgojID09PT09PT09PT09PT09PT09PT0gU1RSSU5HUyA9PT09PT09PT09PT0KUFBfVE9PX1NNT0wgPSAiKirimbDvuJnYp9mE2LXZiNix2Kkg2LXYutmK2LHYqSDYrNiv2YvYpyoqICIKUFBfRVJST1IgPSAiKirimbDvuJnZgdi02YQg2KPYq9mG2KfYoSDZhdi52KfZhNis2Kkg2KfZhNi12YjYsdipKiogIgpOT19BRE1JTiA9ICIqKuKZsO+4mdij2YbYpyDZhNiz2Kog2YXYtNix2YEg2YfZhtinISEqKiAiCk5PX1BFUk0gPSAiKirimbDvuJnZhNmK2LMg2YTYr9mKINij2LDZiNmG2KfYqiDZg9in2YHZitipISoqICIKQ0hBVF9QUF9DSEFOR0VEID0gIioq4pmw77iZ2KrZhSDYqti62YrZitixINi12YjYsdipINin2YTYr9ix2K/YtNipINio2YbYrNin2K0g4pyFKioiCklOVkFMSURfTUVESUEgPSAiKirimbDvuJnZhdmE2K3ZgiDYutmK2LEg2LXYp9mE2K0qKiAiCgpCQU5ORURfUklHSFRTID0gQ2hhdEJhbm5lZFJpZ2h0cygKICAgIHVudGlsX2RhdGU9Tm9uZSwKICAgIHZpZXdfbWVzc2FnZXM9VHJ1ZSwKICAgIHNlbmRfbWVzc2FnZXM9VHJ1ZSwKICAgIHNlbmRfbWVkaWE9VHJ1ZSwKICAgIHNlbmRfc3RpY2tlcnM9VHJ1ZSwKICAgIHNlbmRfZ2lmcz1UcnVlLAogICAgc2VuZF9nYW1lcz1UcnVlLAogICAgc2VuZF9pbmxpbmU9VHJ1ZSwKICAgIGVtYmVkX2xpbmtzPVRydWUsCikKIyBhZG1pbiBwbHVnaW4gZm9yICBqbXRob24KVU5CQU5fUklHSFRTID0gQ2hhdEJhbm5lZFJpZ2h0cygKICAgIHVudGlsX2RhdGU9Tm9uZSwKICAgIHNlbmRfbWVzc2FnZXM9Tm9uZSwKICAgIHNlbmRfbWVkaWE9Tm9uZSwKICAgIHNlbmRfc3RpY2tlcnM9Tm9uZSwKICAgIHNlbmRfZ2lmcz1Ob25lLAogICAgc2VuZF9nYW1lcz1Ob25lLAogICAgc2VuZF9pbmxpbmU9Tm9uZSwKICAgIGVtYmVkX2xpbmtzPU5vbmUsCikKCkxPR1MgPSBsb2dnaW5nLmdldExvZ2dlcihfX25hbWVfXykKTVVURV9SSUdIVFMgPSBDaGF0QmFubmVkUmlnaHRzKHVudGlsX2RhdGU9Tm9uZSwgc2VuZF9tZXNzYWdlcz1UcnVlKQpVTk1VVEVfUklHSFRTID0gQ2hhdEJhbm5lZFJpZ2h0cyh1bnRpbF9kYXRlPU5vbmUsIHNlbmRfbWVzc2FnZXM9RmFsc2UpCgpwbHVnaW5fY2F0ZWdvcnkgPSAiYWFkbWluIgojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKCkBqbXRob24uYXJfY21kKAogICAgcGF0dGVybj0i2KfZhNi12YjYsdipKCAt2YjYtti5fCAt2K3YsNmBKSQiLAogICAgY29tbWFuZD0oItin2YTYtdmI2LHYqSIsIHBsdWdpbl9jYXRlZ29yeSksCiAgICBpbmZvPXsKICAgICAgICAi4pmw77iZ2KfZhNij2LPZgNiq2K7Yr9in2YUiOiAiRm9yIGNoYW5naW5nIGdyb3VwIGRpc3BsYXkgcGljIG9yIGRlbGV0aW5nIGRpc3BsYXkgcGljIiwKICAgICAgICAi4pmw77iZ2KfZhNi02YDYsditIjogIlJlcGx5IHRvIEltYWdlIGZvciBjaGFuZ2luZyBkaXNwbGF5IHBpY3R1cmUiLAogICAgICAgICJmbGFncyI6IHsKICAgICAgICAgICAgIi1zIjogIlRvIHNldCBncm91cCBwaWMiLAogICAgICAgICAgICAiLWQiOiAiVG8gZGVsZXRlIGdyb3VwIHBpYyIsCiAgICAgICAgfSwKICAgICAgICAi4pmw77iZ2KfZhNij2YXZgNixIjogWwogICAgICAgICAgICAie3Ryfdin2YTYtdmI2LHYqSAt2YjYtti5IDxyZXBseSB0byBpbWFnZT4iLAogICAgICAgICAgICAie3RyfWdwaWMgLdit2LDZgSIsCiAgICAgICAgXSwKICAgIH0sCiAgICBncm91cHNfb25seT1UcnVlLAogICAgcmVxdWlyZV9hZG1pbj1UcnVlLAopCmFzeW5jIGRlZiBzZXRfZ3JvdXBfcGhvdG8oZXZlbnQpOiAgIyBzb3VyY2VyeSBuby1tZXRyaWNzCiAgICAiRm9yIGNoYW5naW5nIEdyb3VwIGRwIgogICAgZmxhZyA9IChldmVudC5wYXR0ZXJuX21hdGNoLmdyb3VwKDEpKS5zdHJpcCgpCiAgICBpZiBmbGFnID09ICItcyI6CiAgICAgICAgcmVwbHltc2cgPSBhd2FpdCBldmVudC5nZXRfcmVwbHlfbWVzc2FnZSgpCiAgICAgICAgcGhvdG8gPSBOb25lCiAgICAgICAgaWYgcmVwbHltc2cgYW5kIHJlcGx5bXNnLm1lZGlhOgogICAgICAgICAgICBpZiBpc2luc3RhbmNlKHJlcGx5bXNnLm1lZGlhLCBNZXNzYWdlTWVkaWFQaG90byk6CiAgICAgICAgICAgICAgICBwaG90byA9IGF3YWl0IGV2ZW50LmNsaWVudC5kb3dubG9hZF9tZWRpYShtZXNzYWdlPXJlcGx5bXNnLnBob3RvKQogICAgICAgICAgICBlbGlmICJpbWFnZSIgaW4gcmVwbHltc2cubWVkaWEuZG9jdW1lbnQubWltZV90eXBlLnNwbGl0KCIvIik6CiAgICAgICAgICAgICAgICBwaG90byA9IGF3YWl0IGV2ZW50LmNsaWVudC5kb3dubG9hZF9maWxlKHJlcGx5bXNnLm1lZGlhLmRvY3VtZW50KQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgcmV0dXJuIGF3YWl0IGVkaXRfZGVsZXRlKGV2ZW50LCBJTlZBTElEX01FRElBKQogICAgICAgIGlmIHBob3RvOgogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICBhd2FpdCBldmVudC5jbGllbnQoCiAgICAgICAgICAgICAgICAgICAgRWRpdFBob3RvUmVxdWVzdCgKICAgICAgICAgICAgICAgICAgICAgICAgZXZlbnQuY2hhdF9pZCwgYXdhaXQgZXZlbnQuY2xpZW50LnVwbG9hZF9maWxlKHBob3RvKQogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIGF3YWl0IGVkaXRfZGVsZXRlKGV2ZW50LCBDSEFUX1BQX0NIQU5HRUQpCiAgICAgICAgICAgIGV4Y2VwdCBQaG90b0Nyb3BTaXplU21hbGxFcnJvcjoKICAgICAgICAgICAgICAgIHJldHVybiBhd2FpdCBlZGl0X2RlbGV0ZShldmVudCwgUFBfVE9PX1NNT0wpCiAgICAgICAgICAgIGV4Y2VwdCBJbWFnZVByb2Nlc3NGYWlsZWRFcnJvcjoKICAgICAgICAgICAgICAgIHJldHVybiBhd2FpdCBlZGl0X2RlbGV0ZShldmVudCwgUFBfRVJST1IpCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICAgICAgICAgIHJldHVybiBhd2FpdCBlZGl0X2RlbGV0ZShldmVudCwgZiIqKtiu2YDYt9ijIDogKipge3N0cihlKX1gIikKICAgICAgICAgICAgcHJvY2VzcyA9ICJ1cGRhdGVkIgogICAgZWxzZToKICAgICAgICB0cnk6CiAgICAgICAgICAgIGF3YWl0IGV2ZW50LmNsaWVudChFZGl0UGhvdG9SZXF1ZXN0KGV2ZW50LmNoYXRfaWQsIElucHV0Q2hhdFBob3RvRW1wdHkoKSkpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgICAgICByZXR1cm4gYXdhaXQgZWRpdF9kZWxldGUoZXZlbnQsIGYiKirYrtmA2LfYoyA6ICoqYHtzdHIoZSl9YCIpCiAgICAgICAgcHJvY2VzcyA9ICJkZWxldGVkIgogICAgICAgIGF3YWl0IGVkaXRfZGVsZXRlKGV2ZW50LCAiKirimbDvuJnYqtmA2YUg2K3YsNmBINin2YTZgNi12YjYsdipINio2YbZgNis2KfYrSDinIUiKQogICAgaWYgQk9UTE9HOgogICAgICAgIGF3YWl0IGV2ZW50LmNsaWVudC5zZW5kX21lc3NhZ2UoCiAgICAgICAgICAgIEJPVExPR19DSEFUSUQsCiAgICAgICAgICAgICIj2LXZiNix2Ydf2KfZhNmF2KzZhdmI2LnYqVxuIgogICAgICAgICAgICBmIti12YjYsdipINin2YTZhdis2YXZiNi52Ycge3Byb2Nlc3N9INio2YbYrNin2K0gIgogICAgICAgICAgICBmItin2YTYr9ix2K/YtNmHOiB7ZXZlbnQuY2hhdC50aXRsZX0oYHtldmVudC5jaGF0X2lkfWApIiwKICAgICAgICApCgoKQGptdGhvbi5hcl9jbWQoCiAgICBwYXR0ZXJuPSLYsdmB2Lkg2YXYtNix2YEoPzpcc3wkKShbXHNcU10qKSIsCiAgICBjb21tYW5kPSgi2LHZgdi5INmF2LTYsdmBIiwgcGx1Z2luX2NhdGVnb3J5KSwKICAgIGluZm89ewogICAgICAgICLYp9mE2KfZhdixIjogIuKZsO+4mdmE2LHZgdi5INin2YTYtNiu2LUg2YXYtNix2YEg2YXYuSDYtdmE2KfYrdmK2KfYqiIsCiAgICAgICAgItin2YTYtNix2K0iOiAi4pmw77iZ2YTYsdmB2Lkg2KfZhNi02K7YtSDZhdi02LHZgSDYqNin2YTZhdis2YXZiNi52Ycg2YLZhSDYqNin2YTYsdivINi52YTZiSDYp9mE2LTYrti1XAogICAgICAgICAgICBcbuKZsO+4mdiq2YDYrdiq2KfYrCDYp9mE2LXZhNin2K3ZgNmK2KfYqiDZhNmA2YfYsNinINin2YTYo9mF2YDYsSIsCiAgICAgICAgItin2YTYp9iz2KrYrtiv2KfZhSI6IFsKICAgICAgICAgICAgInt0cn3YsdmB2Lkg2YXYtNix2YEgPNin2YrYr9mKL9mF2LnYsdmBL9io2KfZhNix2K8g2LnZhNmK2Yc+IiwKICAgICAgICAgICAgInt0cn3YsdmB2Lkg2YXYtNix2YEgPNin2YrYr9mKL9mF2LnYsdmBL9io2KfZhNix2K8g2LnZhNmK2Yc+ICIsCiAgICAgICAgXSwKICAgIH0sCiAgICBncm91cHNfb25seT1UcnVlLAogICAgcmVxdWlyZV9hZG1pbj1UcnVlLAopICAjIGFkbWluIHBsdWdpbiBmb3IgIGptdGhvbgphc3luYyBkZWYgcHJvbW90ZShldmVudCk6CiAgICAi4pmw77iZ2YTZgNix2YHYuSDZhdiz2KrZgNiu2K/ZhSDZhdi02YDYsdmBINmB2Yog2KfZhNmA2YPYsdmI2KgiCiAgICBuZXdfcmlnaHRzID0gQ2hhdEFkbWluUmlnaHRzKAogICAgICAgIGFkZF9hZG1pbnM9RmFsc2UsCiAgICAgICAgaW52aXRlX3VzZXJzPVRydWUsCiAgICAgICAgY2hhbmdlX2luZm89RmFsc2UsCiAgICAgICAgYmFuX3VzZXJzPVRydWUsCiAgICAgICAgZGVsZXRlX21lc3NhZ2VzPVRydWUsCiAgICAgICAgcGluX21lc3NhZ2VzPVRydWUsCiAgICApCiAgICB1c2VyLCByYW5rID0gYXdhaXQgZ2V0X3VzZXJfZnJvbV9ldmVudChldmVudCkKICAgIGlmIG5vdCByYW5rOgogICAgICAgIHJhbmsgPSAiQWRtaW4iCiAgICBpZiBub3QgdXNlcjoKICAgICAgICByZXR1cm4KICAgIGNhdGV2ZW50ID0gYXdhaXQgZWRpdF9vcl9yZXBseShldmVudCwgIioq2YrZgNiq2YUg2KfZhNix2YHZgNi5KioiKQogICAgdHJ5OgogICAgICAgIGF3YWl0IGV2ZW50LmNsaWVudChFZGl0QWRtaW5SZXF1ZXN0KGV2ZW50LmNoYXRfaWQsIHVzZXIuaWQsIG5ld19yaWdodHMsIHJhbmspKQogICAgZXhjZXB0IEJhZFJlcXVlc3RFcnJvcjoKICAgICAgICByZXR1cm4gYXdhaXQgY2F0ZXZlbnQuZWRpdChOT19QRVJNKQogICAgYXdhaXQgY2F0ZXZlbnQuZWRpdCgiKirYqtmFINix2YHYudmHINmF2LTYsdmBINio2KfZhNmF2KzZhdmI2LnZhyDYqNmG2KzYp9itIOKchSoqIikKICAgIGlmIEJPVExPRzoKICAgICAgICBhd2FpdCBldmVudC5jbGllbnQuc2VuZF9tZXNzYWdlKAogICAgICAgICAgICBCT1RMT0dfQ0hBVElELAogICAgICAgICAgICBmIiPYp9mE2YDYsdmB2YDYuVwKICAgICAgICAgICAgXG7Yp9mE2YDZhdiz2KrYrtmA2K/ZhTogW3t1c2VyLmZpcnN0X25hbWV9XSh0ZzovL3VzZXI/aWQ9e3VzZXIuaWR9KVwKICAgICAgICAgICAgXG7Yp9mE2YDYr9ix2K/YtNmA2Kk6IHtldmVudC5jaGF0LnRpdGxlfSAoYHtldmVudC5jaGF0X2lkfWApIiwKICAgICAgICApCgoKQGptdGhvbi5hcl9jbWQoCiAgICBwYXR0ZXJuPSLYqtmDKD86XHN8JCkoW1xzXFNdKikiLAogICAgY29tbWFuZD0oItiq2YMiLCBwbHVnaW5fY2F0ZWdvcnkpLAogICAgaW5mbz17CiAgICAgICAgItin2YTYp9mF2LEiOiAi4pmw77iZ2YTYqtmG2LLZitmEINin2YTYtNiu2LUg2YPZhiDYp9mE2KfYtNix2KfZgSIsCiAgICAgICAgItin2YTYtNix2K0iOiAi4pmw77iZ2YrZgtmI2YUg2YfYsNinINin2YTYp9mF2LEg2KjYrdiw2YEg2KzZhdmK2Lkg2LXZhNin2K3Zitin2Kog2KfZhNmF2LTYsdmBXAogICAgICAgICAgICBcbuKZsO+4mdmF2YTYp9it2LjZhyA6KirZhNin2LLZhSDYqtmD2YjZhiDYp9mG2Kog2KfZhNi02K7YtSDYp9mE2Yog2LHZgdi52Ycg2KfZiCDYqtmD2YjZhiDZhdin2YTZgyDYp9mE2YXYrNmF2YjYudmHINit2KrZiSDYqtmG2LLZhNmHKioiLAogICAgICAgICLYp9mE2KfYs9iq2K7Yr9in2YUiOiBbCiAgICAgICAgICAgICJ7dHJ92KrZgyA82KfZhNin2YrYr9mKL9in2YTZhdi52LHZgS/YqNin2YTYsdivINi52YTZitmHPiIsCiAgICAgICAgICAgICJ7dHJ92KrZgyA82KfZhNin2YrYr9mKL9in2YTZhdi52LHZgS/YqNin2YTYsdivINi52YTZitmHPiIsCiAgICAgICAgXSwKICAgIH0sCiAgICBncm91cHNfb25seT1UcnVlLAogICAgcmVxdWlyZV9hZG1pbj1UcnVlLAopCmFzeW5jIGRlZiBkZW1vdGUoZXZlbnQpOgogICAgIuKZsO+4mdmE2YDYqtmG2LLZitmA2YQg2LTZgNiu2LUg2YXZhiDYp9mE2KPYtNmA2LHYp9mBIgogICAgdXNlciwgXyA9IGF3YWl0IGdldF91c2VyX2Zyb21fZXZlbnQoZXZlbnQpCiAgICBpZiBub3QgdXNlcjoKICAgICAgICByZXR1cm4KICAgIGNhdGV2ZW50ID0gYXdhaXQgZWRpdF9vcl9yZXBseShldmVudCwgIioq4pmw77iZ2YrZgNiq2YUg2KfZhNiq2YbYstmK2YQg2YXZhiDYp9mE2KfYtNix2KfZgSoqIikKICAgIG5ld3JpZ2h0cyA9IENoYXRBZG1pblJpZ2h0cygKICAgICAgICBhZGRfYWRtaW5zPU5vbmUsCiAgICAgICAgaW52aXRlX3VzZXJzPU5vbmUsCiAgICAgICAgY2hhbmdlX2luZm89Tm9uZSwKICAgICAgICBiYW5fdXNlcnM9Tm9uZSwKICAgICAgICBkZWxldGVfbWVzc2FnZXM9Tm9uZSwKICAgICAgICBwaW5fbWVzc2FnZXM9Tm9uZSwKICAgICkKICAgIHJhbmsgPSAiYWRtaW4iCiAgICB0cnk6CiAgICAgICAgYXdhaXQgZXZlbnQuY2xpZW50KEVkaXRBZG1pblJlcXVlc3QoZXZlbnQuY2hhdF9pZCwgdXNlci5pZCwgbmV3cmlnaHRzLCByYW5rKSkKICAgIGV4Y2VwdCBCYWRSZXF1ZXN0RXJyb3I6CiAgICAgICAgcmV0dXJuIGF3YWl0IGNhdGV2ZW50LmVkaXQoTk9fUEVSTSkKICAgIGF3YWl0IGNhdGV2ZW50LmVkaXQoIioq4pmw77iZ2KrZgNmFINiq2YbYstmK2YTZhyDZhdmGINmC2KfYptmF2Ycg2KfZhNin2K/ZhdmG2YrZhyDYqNmG2KzYp9itIOKchSoqIikKICAgIGlmIEJPVExPRzoKICAgICAgICBhd2FpdCBldmVudC5jbGllbnQuc2VuZF9tZXNzYWdlKAogICAgICAgICAgICBCT1RMT0dfQ0hBVElELAogICAgICAgICAgICBmIiPYqtmG2LLZitmEX9mF2LTYsdmBXAogICAgICAgICAgICBcbtin2YTZhdi52LHZgTogW3t1c2VyLmZpcnN0X25hbWV9XSh0ZzovL3VzZXI/aWQ9e3VzZXIuaWR9KVwKICAgICAgICAgICAgXG7Yp9mE2K/Ysdiv2LTZhzoge2V2ZW50LmNoYXQudGl0bGV9KGB7ZXZlbnQuY2hhdF9pZH1gKSIsCiAgICAgICAgKQoKCkBqbXRob24uYXJfY21kKAogICAgcGF0dGVybj0i2LfYsdivKD86XHN8JCkoW1xzXFNdKikiLAogICAgY29tbWFuZD0oIti32LHYryIsIHBsdWdpbl9jYXRlZ29yeSksCiAgICBpbmZvPXsKICAgICAgICAi4pmw77iZ2KfZhNij2LPZgNiq2K7Yr9in2YUiOiAi2YTZgNi32LHYryDYtNmA2K7YtiDZhdmGINin2YTZgNmD2LHZiNioIiwKICAgICAgICAi4pmw77iZ2KfZhNi02YDYsditIjogItmE2YDYt9ix2K8g2LTYrti1INmF2YYg2KfZhNmF2YDYrNmF2YjYudipINmK2LPYqti32YrYuSDYp9mE2KPZhti22YDZhdin2YUg2YXYsdipINin2K7ZgNix2YkuXAogICAgICAgIFxu4pmw77iZ2KrZgNit2KrYp9isINin2YTYtdmE2KfYrdmA2YrYp9iqINmE2YDZh9iw2Kcg2KfZhNij2YXZgNixLiIsCiAgICAgICAgIuKZsO+4mdin2YTYo9mF2YDYsSI6IFsKICAgICAgICAgICAgInt0cn3Yt9ix2K8gPNin2YTYp9mK2K/Zii/Yp9mE2YXYudix2YEv2KjYp9mE2LHYryDYudmE2YrZhz4iLAogICAgICAgICAgICAie3Ryfdi32LHYryA82KfZhNin2YrYr9mKL9in2YTZhdi52LHZgS/YqNin2YTYsdivINi52YTZitmHPiA82KfZhNiz2KjYqD4gIiwKICAgICAgICBdLAogICAgfSwKICAgIGdyb3Vwc19vbmx5PVRydWUsCiAgICByZXF1aXJlX2FkbWluPVRydWUsCikKYXN5bmMgZGVmIGVuZG11dGUoZXZlbnQpOgogICAgItmE2YDYt9ix2K8g2LTZgNiu2LYg2YXZhiDYp9mE2YDZg9ix2YjYqCIKICAgIHVzZXIsIHJlYXNvbiA9IGF3YWl0IGdldF91c2VyX2Zyb21fZXZlbnQoZXZlbnQpCiAgICBpZiBub3QgdXNlcjoKICAgICAgICByZXR1cm4KICAgIGNhdGV2ZW50ID0gYXdhaXQgZWRpdF9vcl9yZXBseShldmVudCwgIuKZsO+4mdmK2YDYqtmFINi32YDYsdivINin2YTZgNmF2LPYqtiu2K/ZhSDYo9mG2KrZgNi42LEiKQogICAgdHJ5OgogICAgICAgIGF3YWl0IGV2ZW50LmNsaWVudC5raWNrX3BhcnRpY2lwYW50KGV2ZW50LmNoYXRfaWQsIHVzZXIuaWQpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgcmV0dXJuIGF3YWl0IGNhdGV2ZW50LmVkaXQoTk9fUEVSTSArIGYiXG57c3RyKGUpfSIpCiAgICBpZiByZWFzb246CiAgICAgICAgYXdhaXQgY2F0ZXZlbnQuZWRpdCgKICAgICAgICAgICAgZiLimbDvuJnYp9mE2YDZhdiz2KrYrtiv2YUgW3t1c2VyLmZpcnN0X25hbWV9XSh0ZzovL3VzZXI/aWQ9e3VzZXIuaWR9KVxuIOKZsO+4mdiq2YDZhSDYt9ix2K/ZhyDYqNmG2KzYp9itIOKchSBcbuKZsO+4mdin2YTYs9mA2KjYqCA6IHtyZWFzb259IgogICAgICAgICkKICAgIGVsc2U6CiAgICAgICAgYXdhaXQgY2F0ZXZlbnQuZWRpdCgKICAgICAgICAgICAgZiLimbDvuJnYp9mE2YDZhdiz2KrYrtiv2YUgW3t1c2VyLmZpcnN0X25hbWV9XSh0ZzovL3VzZXI/aWQ9e3VzZXIuaWR9KVxuIOKZsO+4mdiq2YDZhSDYt9ix2K/ZhyDYqNmG2KzYp9itIOKchSAiCiAgICAgICAgKQoKCkBqbXRob24uYXJfY21kKAogICAgcGF0dGVybj0i2K3YuNixKD86XHN8JCkoW1xzXFNdKikiLAogICAgY29tbWFuZD0oItit2LjYsSIsIHBsdWdpbl9jYXRlZ29yeSksCiAgICBpbmZvPXsKICAgICAgICAi4pmw77iZ2KfZhNin2LPYqtiu2K/Yp9mFIjogItmK2YLZgNmI2YUg2KjZgNit2LjYsSDYtNiu2YDYtSDZgdmKINin2YTZgNmD2LHZiNioINin2YTYodmKINin2LPZgNiq2K7Yr9mF2Kog2YHZitmA2Ycg2KfZhNin2YXYsS4iLAogICAgICAgICLimbDvuJnYp9mE2LTYsditIjogItmE2K3ZgNi42LEg2LTYrtmA2LUg2YXZhiDYp9mE2YPZgNix2YjYqCDZiNmF2YDZhti52Ycg2YXZhiDYp9mE2KPZhtmA2LbZhdin2YUg2YXYrNmA2K/Yr9inXAogICAgICAgICAgICBcbuKZsO+4mdiq2YDYrdiq2KfYrCDYp9mE2LXZhNin2K3ZgNmK2KfYqiDZhNmA2YfYsNinINin2YTYo9mF2YDYsS4iLAogICAgICAgICLimbDvuJnYp9mE2KfZhdixIjogWwogICAgICAgICAgICAie3Ryfdit2LjYsSA82KfZhNin2YrYr9mKL9in2YTZhdi52LHZgS/YqNin2YTYsdivINi52YTZitmHPiIsCiAgICAgICAgICAgICJ7dHJ92K3YuNixIDzYp9mE2KfZitiv2Yov2KfZhNmF2LnYsdmBL9io2KfZhNix2K8g2LnZhNmK2Yc+IDzYp9mE2LPYqNioPiIsCiAgICAgICAgXSwKICAgIH0sCiAgICBncm91cHNfb25seT1UcnVlLAogICAgcmVxdWlyZV9hZG1pbj1UcnVlLAopCmFzeW5jIGRlZiBfYmFuX3BlcnNvbihldmVudCk6CiAgICAi4pmw77iZ2YTYrdmA2LjYsSDYtNiu2LUg2YHZiiDZg9mA2LHZiNioINmF2YDYudmK2YYiCiAgICB1c2VyLCByZWFzb24gPSBhd2FpdCBnZXRfdXNlcl9mcm9tX2V2ZW50KGV2ZW50KQogICAgaWYgbm90IHVzZXI6CiAgICAgICAgcmV0dXJuCiAgICBpZiB1c2VyLmlkID09IDE3MTUwNTE2MTY6CiAgICAgICAgcmV0dXJuIGF3YWl0IGVkaXRfZGVsZXRlKGV2ZW50LCAiKiotINmE2Kcg2YrZhdqq2YbZhtmKINit2LjYsSDZg9ix2YjYqNmKINiv2Yog2YTZgyoqIikKICAgIGlmIHVzZXIuaWQgPT0gMTY5NDM4NjU2MToKICAgICAgICByZXR1cm4gYXdhaXQgZWRpdF9kZWxldGUoZXZlbnQsICIqKi0g2YTYpyDZitmF2qrZhtmG2Yog2K3YuNixINmD2LHZiNio2Yog2K/ZiiDZhNmDKioiKQogICAgaWYgdXNlci5pZCA9PSAxNjU3OTMzNjgwOgogICAgICAgIHJldHVybiBhd2FpdCBlZGl0X2RlbGV0ZShldmVudCwgIioqLSDZhNinINmK2YXaqtmG2YbZiiDYrdi42LEg2YPYsdmI2KjZiiDYr9mKINmE2YMqKiIpCiAgICBjYXRldmVudCA9IGF3YWl0IGVkaXRfb3JfcmVwbHkoZXZlbnQsICLimbDvuJnYqtmA2YUg2K3ZgNi42LHZhyDYqNmA2YbYrNin2K0iKQogICAgdHJ5OgogICAgICAgIGF3YWl0IGV2ZW50LmNsaWVudChFZGl0QmFubmVkUmVxdWVzdChldmVudC5jaGF0X2lkLCB1c2VyLmlkLCBCQU5ORURfUklHSFRTKSkKICAgIGV4Y2VwdCBCYWRSZXF1ZXN0RXJyb3I6CiAgICAgICAgcmV0dXJuIGF3YWl0IGNhdGV2ZW50LmVkaXQoTk9fUEVSTSkKICAgIHRyeToKICAgICAgICByZXBseSA9IGF3YWl0IGV2ZW50LmdldF9yZXBseV9tZXNzYWdlKCkKICAgICAgICBpZiByZXBseToKICAgICAgICAgICAgYXdhaXQgcmVwbHkuZGVsZXRlKCkKICAgIGV4Y2VwdCBCYWRSZXF1ZXN0RXJyb3I6CiAgICAgICAgcmV0dXJuIGF3YWl0IGNhdGV2ZW50LmVkaXQoIuKZsO+4mdmE2YrZgNizINmE2YDYr9mKINis2YDZhdmK2Lkg2KfZhNi12YDZhNin2K3ZitmA2KfYqiDZhNmD2YDZhiDYs9mK2YDYqNmC2Ykg2YXYrdmA2LjZiNixIikKICAgIGlmIHJlYXNvbjoKICAgICAgICBhd2FpdCBjYXRldmVudC5lZGl0KAogICAgICAgICAgICBmIuKZsO+4mdin2YTZhdiz2YDYqtiu2K/ZhSB7X2Zvcm1hdC5tZW50aW9udXNlcih1c2VyLmZpcnN0X25hbWUgLHVzZXIuaWQpfSBcbiDimbDvuJnYqtmA2YUg2K3ZgNi42LHZhyDYqNmG2YDYrNin2K0gISFcbioq4pmw77iZ2KfZhNiz2KjYqCA6ICoqYHtyZWFzb259YCIKICAgICAgICApCiAgICBlbHNlOgogICAgICAgIGF3YWl0IGNhdGV2ZW50LmVkaXQoCiAgICAgICAgICAgIGYi4pmw77iZ2KfZhNmF2LPZgNiq2K7Yr9mFIHtfZm9ybWF0Lm1lbnRpb251c2VyKHVzZXIuZmlyc3RfbmFtZSAsdXNlci5pZCl9IFxuIOKZsO+4mdiq2YDZhSDYrdmA2LjYsdmHINio2YbZgNis2KfYrSDinIUiCiAgICAgICAgKQogICAgaWYgQk9UTE9HOgogICAgICAgIGlmIHJlYXNvbjoKICAgICAgICAgICAgYXdhaXQgZXZlbnQuY2xpZW50LnNlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgIEJPVExPR19DSEFUSUQsCiAgICAgICAgICAgICAgICBmIuKZsO+4mdin2YTYrdmA2LjYsVwKICAgICAgICAgICAgICAgIFxu2KfZhNmF2LPZgNiq2K7Yr9mFOiBbe3VzZXIuZmlyc3RfbmFtZX1dKHRnOi8vdXNlcj9pZD17dXNlci5pZH0pXAogICAgICAgICAgICAgICAgXG7Yp9mE2YDYr9ix2K/YtNmA2Kk6IHtldmVudC5jaGF0LnRpdGxlfVwKICAgICAgICAgICAgICAgIFxu2KfZitiv2Yog2KfZhNmD2LHZiNioKGB7ZXZlbnQuY2hhdF9pZH1gKVwKICAgICAgICAgICAgICAgIFxu2KfZhNiz2KjZgNioIDoge3JlYXNvbn0iLAogICAgICAgICAgICApCiAgICAgICAgZWxzZToKICAgICAgICAgICAgYXdhaXQgZXZlbnQuY2xpZW50LnNlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgIEJPVExPR19DSEFUSUQsCiAgICAgICAgICAgICAgICBmIuKZsO+4mdin2YTYrdmA2LjYsVwKICAgICAgICAgICAgICAgIFxu2KfZhNmF2LPZgNiq2K7Yr9mFOiBbe3VzZXIuZmlyc3RfbmFtZX1dKHRnOi8vdXNlcj9pZD17dXNlci5pZH0pXAogICAgICAgICAgICAgICAgXG7Yp9mE2YDYr9ix2K/YtNmA2Kk6IHtldmVudC5jaGF0LnRpdGxlfVwKICAgICAgICAgICAgICAgIFxuINin2YrZgNiv2Yog2KfZhNmD2YDYsdmI2Kg6IChge2V2ZW50LmNoYXRfaWR9YCkiLAogICAgICAgICAgICApCgoKQGptdGhvbi5hcl9jbWQoCiAgICBwYXR0ZXJuPSLYp9mE2LrYp9ihINit2LjYsSg/OlxzfCQpKFtcc1xTXSopIiwKICAgIGNvbW1hbmQ9KCLYp9mE2LrYp9ihINit2LjYsSIsIHBsdWdpbl9jYXRlZ29yeSksCiAgICBpbmZvPXsKICAgICAgICAi4pmw77iZ2KfZhNij2LPZgNiq2K7Yr9in2YUiOiAi2YrZgtmA2YjZhSDYqNmA2KfZhNi62KfYoSDYrdmA2LjYsSDYp9mE2LTZgNiu2LUg2YHZiiDYp9mE2YDZg9ix2YjYqCDYp9mE2LDZiiDYp9iz2YDYqtiu2K/ZhdiqINmB2YrZgNmHINin2YTYp9mF2LEuIiwKICAgICAgICAi4pmw77iZ2KfZhNi02LHYrSI6ICLZhNij2YTZgNi62KfYoSDYrdmA2LjYsSDYtNiu2YDYtSDZhdmGINin2YTZg9mA2LHZiNioINmI2KfZhNiz2YDZhdin2K0g2YTZhyDZhdmGINin2YTYo9mG2YDYttmF2KfZhSDZhdis2YDYr9iv2KdcCiAgICAgICAgICAgIFxu4pmw77iZ2KrZgNit2KrYp9isINin2YTYtdmE2KfYrdmA2YrYp9iqINmE2YDZh9iw2Kcg2KfZhNij2YXZgNixLiIsCiAgICAgICAgIuKZsO+4mdin2YTYo9mF2YDYsSI6IFsKICAgICAgICAgICAgInt0cn3Yp9mE2LrYp9ihINit2LjYsSA82KfZhNin2YrYr9mKL9in2YTZhdi52LHZgS/YqNin2YTYsdivINi52YTZitmHPiIsCiAgICAgICAgICAgICJ7dHJ92KfZhNi62KfYoSDYrdi42LEgPNin2YTYp9mK2K/Zii/Yp9mE2YXYudix2YEv2KjYp9mE2LHYryDYudmE2YrZhz4gPNin2YTYs9io2Kg+ICIsCiAgICAgICAgXSwKICAgIH0sCiAgICBncm91cHNfb25seT1UcnVlLAogICAgcmVxdWlyZV9hZG1pbj1UcnVlLAopCmFzeW5jIGRlZiBub3RoYW5vcyhldmVudCk6CiAgICAi4pmw77iZ2YTYo9mE2YDYutin2KEg2KfZhNmA2K3YuNixINmE2YDYtNiu2LUg2YHZiiDZg9mA2LHZiNioINmF2YDYudmK2YYiCiAgICB1c2VyLCBfID0gYXdhaXQgZ2V0X3VzZXJfZnJvbV9ldmVudChldmVudCkKICAgIGlmIG5vdCB1c2VyOgogICAgICAgIHJldHVybgogICAgY2F0ZXZlbnQgPSBhd2FpdCBlZGl0X29yX3JlcGx5KGV2ZW50LCAi4pmw77iZ2KzZgNin2LEg2KfZhNmA2LrYp9ihINin2YTZgNit2LjYsSDYo9mG2KrZgNi42LEg2LHYrNmA2KfYodinIikKICAgIHRyeToKICAgICAgICBhd2FpdCBldmVudC5jbGllbnQoRWRpdEJhbm5lZFJlcXVlc3QoZXZlbnQuY2hhdF9pZCwgdXNlci5pZCwgVU5CQU5fUklHSFRTKSkKICAgICAgICBhd2FpdCBjYXRldmVudC5lZGl0KAogICAgICAgICAgICBmIuKZsO+4mdin2YTZgNmF2LPYqtiu2K/ZhSB7X2Zvcm1hdC5tZW50aW9udXNlcih1c2VyLmZpcnN0X25hbWUgLHVzZXIuaWQpfVxuIOKZsO+4mdiq2YDZhSDYp9mE2YDYutin2KEg2K3ZgNi42LHZhyDYqNmG2YDYrNin2K0gIgogICAgICAgICkKICAgICAgICBpZiBCT1RMT0c6CiAgICAgICAgICAgIGF3YWl0IGV2ZW50LmNsaWVudC5zZW5kX21lc3NhZ2UoCiAgICAgICAgICAgICAgICBCT1RMT0dfQ0hBVElELAogICAgICAgICAgICAgICAgIuKZsO+4mdin2YTZgNi62KfYoSDYp9mE2YDYrdi42LEgXG4iCiAgICAgICAgICAgICAgICBmItin2YTZgNmF2LPYqtiu2K/ZhTogW3t1c2VyLmZpcnN0X25hbWV9XSh0ZzovL3VzZXI/aWQ9e3VzZXIuaWR9KVxuIgogICAgICAgICAgICAgICAgZiLYp9mE2YDYr9ix2K/YtNmA2Kk6IHtldmVudC5jaGF0LnRpdGxlfShge2V2ZW50LmNoYXRfaWR9YCkiLAogICAgICAgICAgICApCiAgICBleGNlcHQgVXNlcklkSW52YWxpZEVycm9yOgogICAgICAgIGF3YWl0IGNhdGV2ZW50LmVkaXQoIuKZsO+4mdmK2YDYqNiv2Ygg2KPZhiDZh9iw2Ycg2KfZhNmA2LnZhdmE2YrZgNipINiq2YUg2KXZhNi62KfYpNmH2YDYpyIpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgYXdhaXQgY2F0ZXZlbnQuZWRpdChmIioq2K7ZgNi32KMgOioqXG5ge2V9YCIpCgoKQGptdGhvbi5hcl9jbWQoaW5jb21pbmc9VHJ1ZSkKYXN5bmMgZGVmIHdhdGNoZXIoZXZlbnQpOgogICAgaWYgaXNfbXV0ZWQoZXZlbnQuc2VuZGVyX2lkLCBldmVudC5jaGF0X2lkKToKICAgICAgICB0cnk6CiAgICAgICAgICAgIGF3YWl0IGV2ZW50LmRlbGV0ZSgpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgICAgICBMT0dTLmluZm8oc3RyKGUpKQo="
    )
)
