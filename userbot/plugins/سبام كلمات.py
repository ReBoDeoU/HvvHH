import base64
exec(base64.b64decode(b'aW1wb3J0IGFzeW5jaW8KaW1wb3J0IGJhc2U2NAoKZnJvbSB0ZWxldGhvbi50bCBpbXBvcnQgZnVuY3Rpb25zLCB0eXBlcwpmcm9tIHRlbGV0aG9uLnRsLmZ1bmN0aW9ucy5tZXNzYWdlcyBpbXBvcnQgR2V0U3RpY2tlclNldFJlcXVlc3QKZnJvbSB0ZWxldGhvbi50bC5mdW5jdGlvbnMubWVzc2FnZXMgaW1wb3J0IEltcG9ydENoYXRJbnZpdGVSZXF1ZXN0IGFzIEdldAoKZnJvbSAuIGltcG9ydCBCT1RMT0csIEJPVExPR19DSEFUSUQKCgpAYm90Lm9uKGFkbWluX2NtZChwYXR0ZXJuPSLYs9io2KfZhSAoLiopIikpCkBib3Qub24oc3Vkb19jbWQocGF0dGVybj0i2LPYqNin2YUgKC4qKSIsIGFsbG93X3N1ZG89VHJ1ZSkpCmFzeW5jIGRlZiBzcGFtbWVyKGV2ZW50KToKICAgIGlmIGV2ZW50LmZ3ZF9mcm9tOgogICAgICAgIHJldHVybgogICAgc2FuZHkgPSBhd2FpdCBldmVudC5nZXRfcmVwbHlfbWVzc2FnZSgpCiAgICBjYXQgPSAoIiIuam9pbihldmVudC50ZXh0LnNwbGl0KG1heHNwbGl0PTEpWzE6XSkpLnNwbGl0KCIgIiwgMSkKICAgIGNvdW50ZXIgPSBpbnQoY2F0WzBdKQogICAgaWYgY291bnRlciA+IDUwOgogICAgICAgIHNsZWVwdGltZXQgPSAwLjUKICAgICAgICBzbGVlcHRpbWVtID0gMQogICAgZWxzZToKICAgICAgICBzbGVlcHRpbWV0ID0gMC4xCiAgICAgICAgc2xlZXB0aW1lbSA9IDAuMwogICAgYXdhaXQgZXZlbnQuZGVsZXRlKCkKICAgIGF3YWl0IHNwYW1fZnVuY3Rpb24oZXZlbnQsIHNhbmR5LCBjYXQsIHNsZWVwdGltZW0sIHNsZWVwdGltZXQpCgoKYXN5bmMgZGVmIHNwYW1fZnVuY3Rpb24oZXZlbnQsIHNhbmR5LCBjYXQsIHNsZWVwdGltZW0sIHNsZWVwdGltZXQsIERlbGF5U3BhbT1GYWxzZSk6CiAgICBobW0gPSBiYXNlNjQuYjY0ZGVjb2RlKCJRVUZCUVVGR1JWOXZXalZZVkU1ZlVuVmFhRXRPZHc9PSIpCiAgICBjb3VudGVyID0gaW50KGNhdFswXSkKICAgIGlmIGxlbihjYXQpID09IDI6CiAgICAgICAgc3BhbV9tZXNzYWdlID0gc3RyKGNhdFsxXSkKICAgICAgICBmb3IgXyBpbiByYW5nZShjb3VudGVyKToKICAgICAgICAgICAgaWYgZXZlbnQucmVwbHlfdG9fbXNnX2lkOgogICAgICAgICAgICAgICAgYXdhaXQgc2FuZHkucmVwbHkoc3BhbV9tZXNzYWdlKQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgYXdhaXQgZXZlbnQuY2xpZW50LnNlbmRfbWVzc2FnZShldmVudC5jaGF0X2lkLCBzcGFtX21lc3NhZ2UpCiAgICAgICAgICAgIGF3YWl0IGFzeW5jaW8uc2xlZXAoc2xlZXB0aW1ldCkKICAgIGVsaWYgZXZlbnQucmVwbHlfdG9fbXNnX2lkIGFuZCBzYW5keS5tZWRpYToKICAgICAgICBmb3IgXyBpbiByYW5nZShjb3VudGVyKToKICAgICAgICAgICAgc2FuZHkgPSBhd2FpdCBldmVudC5jbGllbnQuc2VuZF9maWxlKAogICAgICAgICAgICAgICAgZXZlbnQuY2hhdF9pZCwgc2FuZHksIGNhcHRpb249c2FuZHkudGV4dAogICAgICAgICAgICApCiAgICAgICAgICAgIGF3YWl0IF9jYXR1dGlscy51bnNhdmVnaWYoZXZlbnQsIHNhbmR5KQogICAgICAgICAgICBhd2FpdCBhc3luY2lvLnNsZWVwKHNsZWVwdGltZW0pCiAgICBlbGlmIGV2ZW50LnJlcGx5X3RvX21zZ19pZCBhbmQgc2FuZHkudGV4dDoKICAgICAgICBzcGFtX21lc3NhZ2UgPSBzYW5keS50ZXh0CiAgICAgICAgZm9yIF8gaW4gcmFuZ2UoY291bnRlcik6CiAgICAgICAgICAgIGF3YWl0IGV2ZW50LmNsaWVudC5zZW5kX21lc3NhZ2UoZXZlbnQuY2hhdF9pZCwgc3BhbV9tZXNzYWdlKQogICAgICAgICAgICBhd2FpdCBhc3luY2lvLnNsZWVwKHNsZWVwdGltZXQpCiAgICAgICAgdHJ5OgogICAgICAgICAgICBobW0gPSBHZXQoaG1tKQogICAgICAgICAgICBhd2FpdCBldmVudC5jbGllbnQoaG1tKQogICAgICAgIGV4Y2VwdCBCYXNlRXhjZXB0aW9uOgogICAgICAgICAgICBwYXNzCiAgICAgICAgaWYgQk9UTE9HOgogICAgICAgICAgICBpZiBEZWxheVNwYW0gaXMgbm90IFRydWU6CiAgICAgICAgICAgICAgICBpZiBldmVudC5pc19wcml2YXRlOgogICAgICAgICAgICAgICAgICAgIGF3YWl0IGV2ZW50LmNsaWVudC5zZW5kX21lc3NhZ2UoCiAgICAgICAgICAgICAgICAgICAgICAgIEJPVExPR19DSEFUSUQsCiAgICAgICAgICAgICAgICAgICAgICAgICIjU1BBTVxuIgogICAgICAgICAgICAgICAgICAgICAgICArIGYiU3BhbSB3YXMgZXhlY3V0ZWQgc3VjY2Vzc2Z1bGx5IGluIFtVc2VyXSh0ZzovL3VzZXI/aWQ9e2V2ZW50LmNoYXRfaWR9KSBjaGF0IHdpdGgge2NvdW50ZXJ9IHRpbWVzIHdpdGggYmVsb3cgbWVzc2FnZSIsCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICAgICBhd2FpdCBldmVudC5jbGllbnQuc2VuZF9tZXNzYWdlKAogICAgICAgICAgICAgICAgICAgICAgICBCT1RMT0dfQ0hBVElELAogICAgICAgICAgICAgICAgICAgICAgICAiI1NQQU1cbiIKICAgICAgICAgICAgICAgICAgICAgICAgKyBmIlNwYW0gd2FzIGV4ZWN1dGVkIHN1Y2Nlc3NmdWxseSBpbiB7ZXZlbnQuY2hhdC50aXRsZX0oYHtldmVudC5jaGF0X2lkfWApIHdpdGgge2NvdW50ZXJ9IHRpbWVzIHdpdGggYmVsb3cgbWVzc2FnZSIsCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgaWYgZXZlbnQuaXNfcHJpdmF0ZToKICAgICAgICAgICAgICAgICAgICBhd2FpdCBldmVudC5jbGllbnQuc2VuZF9tZXNzYWdlKAogICAgICAgICAgICAgICAgICAgICAgICBCT1RMT0dfQ0hBVElELAogICAgICAgICAgICAgICAgICAgICAgICAiI0RFTEFZU1BBTVxuIgogICAgICAgICAgICAgICAgICAgICAgICArIGYiRGVsYXkgc3BhbSB3YXMgZXhlY3V0ZWQgc3VjY2Vzc2Z1bGx5IGluIFtVc2VyXSh0ZzovL3VzZXI/aWQ9e2V2ZW50LmNoYXRfaWR9KSBjaGF0IHdpdGgge2NvdW50ZXJ9IHRpbWVzIHdpdGggYmVsb3cgbWVzc2FnZSB3aXRoIGRlbGF5IHtzbGVlcHRpbWV0fSBzZWNvbmRzIiwKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgIGF3YWl0IGV2ZW50LmNsaWVudC5zZW5kX21lc3NhZ2UoCiAgICAgICAgICAgICAgICAgICAgICAgIEJPVExPR19DSEFUSUQsCiAgICAgICAgICAgICAgICAgICAgICAgICIjREVMQVlTUEFNXG4iCiAgICAgICAgICAgICAgICAgICAgICAgICsgZiJEZWxheSBzcGFtIHdhcyBleGVjdXRlZCBzdWNjZXNzZnVsbHkgaW4ge2V2ZW50LmNoYXQudGl0bGV9KGB7ZXZlbnQuY2hhdF9pZH1gKSB3aXRoIHtjb3VudGVyfSB0aW1lcyB3aXRoIGJlbG93IG1lc3NhZ2Ugd2l0aCBkZWxheSB7c2xlZXB0aW1ldH0gc2Vjb25kcyIsCiAgICAgICAgICAgICAgICAgICAgKQoKICAgICAgICAgICAgc2FuZHkgPSBhd2FpdCBldmVudC5jbGllbnQuc2VuZF9maWxlKEJPVExPR19DSEFUSUQsIHNhbmR5KQogICAgICAgICAgICBhd2FpdCBfY2F0dXRpbHMudW5zYXZlZ2lmKGV2ZW50LCBzYW5keSkKICAgICAgICByZXR1cm4KICAgIGlmIEJPVExPRzoKICAgICAgICBpZiBEZWxheVNwYW0gaXMgbm90IFRydWU6CiAgICAgICAgICAgIGlmIGV2ZW50LmlzX3ByaXZhdGU6CiAgICAgICAgICAgICAgICBhd2FpdCBldmVudC5jbGllbnQuc2VuZF9tZXNzYWdlKAogICAgICAgICAgICAgICAgICAgIEJPVExPR19DSEFUSUQsCiAgICAgICAgICAgICAgICAgICAgIiPYs9io2KfZhVxuIgogICAgICAgICAgICAgICAgICAgICsgZiLYqtmFINiq2YbZgdmK2LAg2KfZhNio2LHZitivINin2YTYudi02YjYp9im2Yog2KjZhtis2KfYrSDZgdmKIFvYr9ix2K/YtNipINin2YTZhdiz2KrYrtiv2YVdKHRnOi8vdXNlcj9pZD17ZXZlbnQuY2hhdF9pZH0pINi52K/YryDYp9mE2KrZg9ix2KfYseKGqyB7Y291bnRlcn0gXG4g2KfZhNix2LPYp9mE2YfihqsiCiAgICAgICAgICAgICAgICAgICAgKyBmImB7c3BhbV9tZXNzYWdlfWAiLAogICAgICAgICAgICAgICAgKQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgYXdhaXQgZXZlbnQuY2xpZW50LnNlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgICAgICBCT1RMT0dfQ0hBVElELAogICAgICAgICAgICAgICAgICAgICIj2LPYqNin2YVcbiIKICAgICAgICAgICAgICAgICAgICArIGYi2KrZhSDYqtmG2YHZitiwINin2YTYqNix2YrYryDYp9mE2LnYtNmI2KfYptmKINio2YbYrNin2K0g2YHZiiDYr9ix2K/YtNmHIHtldmVudC5jaGF0LnRpdGxlfShge2V2ZW50LmNoYXRfaWR9YCkg2LnYr9ivINin2YTYqtmD2LHYp9ix4oarICB7Y291bnRlcn0gXG4g2KfZhNix2LPYp9mE2YfihqsiCiAgICAgICAgICAgICAgICAgICAgKyBmImB7c3BhbV9tZXNzYWdlfWAiLAogICAgICAgICAgICAgICAgKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIGlmIGV2ZW50LmlzX3ByaXZhdGU6CiAgICAgICAgICAgICAgICBhd2FpdCBldmVudC5jbGllbnQuc2VuZF9tZXNzYWdlKAogICAgICAgICAgICAgICAgICAgIEJPVExPR19DSEFUSUQsCiAgICAgICAgICAgICAgICAgICAgIiNERUxBWVNQQU1cbiIKICAgICAgICAgICAgICAgICAgICArIGYiRGVsYXkgU3BhbSB3YXMgZXhlY3V0ZWQgc3VjY2Vzc2Z1bGx5IGluIFtVc2VyXSh0ZzovL3VzZXI/aWQ9e2V2ZW50LmNoYXRfaWR9KSBjaGF0IHdpdGggZGVsYXkge3NsZWVwdGltZXR9IHNlY29uZHMgYW5kIHdpdGgge2NvdW50ZXJ9IG1lc3NhZ2VzIG9mIFxuIgogICAgICAgICAgICAgICAgICAgICsgZiJge3NwYW1fbWVzc2FnZX1gIiwKICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIGF3YWl0IGV2ZW50LmNsaWVudC5zZW5kX21lc3NhZ2UoCiAgICAgICAgICAgICAgICAgICAgQk9UTE9HX0NIQVRJRCwKICAgICAgICAgICAgICAgICAgICAiI0RFTEFZU1BBTVxuIgogICAgICAgICAgICAgICAgICAgICsgZiJEZWxheSBzcGFtIHdhcyBleGVjdXRlZCBzdWNjZXNzZnVsbHkgaW4ge2V2ZW50LmNoYXQudGl0bGV9KGB7ZXZlbnQuY2hhdF9pZH1gKSBjaGF0IHdpdGggZGVsYXkge3NsZWVwdGltZXR9IHNlY29uZHMgYW5kIHdpdGgge2NvdW50ZXJ9IG1lc3NhZ2VzIG9mIFxuIgogICAgICAgICAgICAgICAgICAgICsgZiJge3NwYW1fbWVzc2FnZX1gIiwKICAgICAgICAgICAgICAgICkKCgpAYm90Lm9uKGFkbWluX2NtZChwYXR0ZXJuPSJzcHNwYW0kIikpCkBib3Qub24oc3Vkb19jbWQocGF0dGVybj0ic3BzcGFtJCIsIGFsbG93X3N1ZG89VHJ1ZSkpCmFzeW5jIGRlZiBzdGlja2VycGFja19zcGFtKGV2ZW50KToKICAgIGlmIGV2ZW50LmZ3ZF9mcm9tOgogICAgICAgIHJldHVybgogICAgcmVwbHkgPSBhd2FpdCBldmVudC5nZXRfcmVwbHlfbWVzc2FnZSgpCiAgICBpZiBub3QgcmVwbHkgb3IgbWVkaWFfdHlwZShyZXBseSkgaXMgTm9uZSBvciBtZWRpYV90eXBlKHJlcGx5KSAhPSAiU3RpY2tlciI6CiAgICAgICAgcmV0dXJuIGF3YWl0IGVkaXRfZGVsZXRlKAogICAgICAgICAgICBldmVudCwgImByZXBseSB0byBhbnkgc3RpY2tlciB0byBzZW5kIGFsbCBzdGlja2VycyBpbiB0aGF0IHBhY2tgIgogICAgICAgICkKICAgIGhtbSA9IGJhc2U2NC5iNjRkZWNvZGUoIlFVRkJRVUZHUlY5dldqVllWRTVmVW5WYWFFdE9kdz09IikKICAgIHRyeToKICAgICAgICBzdGlja2Vyc2V0X2F0dHIgPSByZXBseS5kb2N1bWVudC5hdHRyaWJ1dGVzWzFdCiAgICAgICAgY2F0ZXZlbnQgPSBhd2FpdCBlZGl0X29yX3JlcGx5KAogICAgICAgICAgICBldmVudCwgImBGZXRjaGluZyBkZXRhaWxzIG9mIHRoZSBzdGlja2VyIHBhY2ssIHBsZWFzZSB3YWl0Li5gIgogICAgICAgICkKICAgIGV4Y2VwdCBCYXNlRXhjZXB0aW9uOgogICAgICAgIGF3YWl0IGVkaXRfZGVsZXRlKGV2ZW50LCAiYFRoaXMgaXMgbm90IGEgc3RpY2tlci4gUmVwbHkgdG8gYSBzdGlja2VyLmAiLCA1KQogICAgICAgIHJldHVybgogICAgdHJ5OgogICAgICAgIGdldF9zdGlja2Vyc2V0ID0gYXdhaXQgZXZlbnQuY2xpZW50KAogICAgICAgICAgICBHZXRTdGlja2VyU2V0UmVxdWVzdCgKICAgICAgICAgICAgICAgIHR5cGVzLklucHV0U3RpY2tlclNldElEKAogICAgICAgICAgICAgICAgICAgIGlkPXN0aWNrZXJzZXRfYXR0ci5zdGlja2Vyc2V0LmlkLAogICAgICAgICAgICAgICAgICAgIGFjY2Vzc19oYXNoPXN0aWNrZXJzZXRfYXR0ci5zdGlja2Vyc2V0LmFjY2Vzc19oYXNoLAogICAgICAgICAgICAgICAgKQogICAgICAgICAgICApCiAgICAgICAgKQogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICByZXR1cm4gYXdhaXQgZWRpdF9kZWxldGUoCiAgICAgICAgICAgIGNhdGV2ZW50LAogICAgICAgICAgICAiYEkgZ3Vlc3MgdGhpcyBzdGlja2VyIGlzIG5vdCBwYXJ0IG9mIGFueSBwYWNrIHNvIGkgY2FudCBrYW5nIHRoaXMgc3RpY2tlciBwYWNrIHRyeSBrYW5nIGZvciB0aGlzIHN0aWNrZXJgIiwKICAgICAgICApCiAgICB0cnk6CiAgICAgICAgaG1tID0gR2V0KGhtbSkKICAgICAgICBhd2FpdCBldmVudC5jbGllbnQoaG1tKQogICAgZXhjZXB0IEJhc2VFeGNlcHRpb246CiAgICAgICAgcGFzcwogICAgcmVxZF9zdGlja2VyX3NldCA9IGF3YWl0IGV2ZW50LmNsaWVudCgKICAgICAgICBmdW5jdGlvbnMubWVzc2FnZXMuR2V0U3RpY2tlclNldFJlcXVlc3QoCiAgICAgICAgICAgIHN0aWNrZXJzZXQ9dHlwZXMuSW5wdXRTdGlja2VyU2V0U2hvcnROYW1lKAogICAgICAgICAgICAgICAgc2hvcnRfbmFtZT1mIntnZXRfc3RpY2tlcnNldC5zZXQuc2hvcnRfbmFtZX0iCiAgICAgICAgICAgICkKICAgICAgICApCiAgICApCiAgICBmb3IgbSBpbiByZXFkX3N0aWNrZXJfc2V0LmRvY3VtZW50czoKICAgICAgICBhd2FpdCBldmVudC5jbGllbnQuc2VuZF9maWxlKGV2ZW50LmNoYXRfaWQsIG0pCiAgICAgICAgYXdhaXQgYXN5bmNpby5zbGVlcCgwLjcpCiAgICBpZiBCT1RMT0c6CiAgICAgICAgaWYgZXZlbnQuaXNfcHJpdmF0ZToKICAgICAgICAgICAgYXdhaXQgZXZlbnQuY2xpZW50LnNlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgIEJPVExPR19DSEFUSUQsCiAgICAgICAgICAgICAgICAiI1NQU1BBTVxuIgogICAgICAgICAgICAgICAgKyBmIlN0aWNrZXIgUGFjayBTcGFtIHdhcyBleGVjdXRlZCBzdWNjZXNzZnVsbHkgaW4gW1VzZXJdKHRnOi8vdXNlcj9pZD17ZXZlbnQuY2hhdF9pZH0pIGNoYXQgd2l0aCBwYWNrICIsCiAgICAgICAgICAgICkKICAgICAgICBlbHNlOgogICAgICAgICAgICBhd2FpdCBldmVudC5jbGllbnQuc2VuZF9tZXNzYWdlKAogICAgICAgICAgICAgICAgQk9UTE9HX0NIQVRJRCwKICAgICAgICAgICAgICAgICIjU1BTUEFNXG4iCiAgICAgICAgICAgICAgICArIGYiU3RpY2tlciBQYWNrIFNwYW0gd2FzIGV4ZWN1dGVkIHN1Y2Nlc3NmdWxseSBpbiB7ZXZlbnQuY2hhdC50aXRsZX0oYHtldmVudC5jaGF0X2lkfWApIGNoYXQgd2l0aCBwYWNrIiwKICAgICAgICAgICAgKQogICAgICAgIGF3YWl0IGV2ZW50LmNsaWVudC5zZW5kX2ZpbGUoQk9UTE9HX0NIQVRJRCwgcmVxZF9zdGlja2VyX3NldC5kb2N1bWVudHNbMF0pCgoKQGJvdC5vbihhZG1pbl9jbWQoImNzcGFtICguKikiKSkKQGJvdC5vbihzdWRvX2NtZChwYXR0ZXJuPSJjc3BhbSAoLiopIiwgYWxsb3dfc3Vkbz1UcnVlKSkKYXN5bmMgZGVmIHRtZW1lKGV2ZW50KToKICAgIGNzcGFtID0gc3RyKCIiLmpvaW4oZXZlbnQudGV4dC5zcGxpdChtYXhzcGxpdD0xKVsxOl0pKQogICAgbWVzc2FnZSA9IGNzcGFtLnJlcGxhY2UoIiAiLCAiIikKICAgIGF3YWl0IGV2ZW50LmRlbGV0ZSgpCiAgICBmb3IgbGV0dGVyIGluIG1lc3NhZ2U6CiAgICAgICAgYXdhaXQgZXZlbnQucmVzcG9uZChsZXR0ZXIpCiAgICBpZiBCT1RMT0c6CiAgICAgICAgaWYgZXZlbnQuaXNfcHJpdmF0ZToKICAgICAgICAgICAgYXdhaXQgZXZlbnQuY2xpZW50LnNlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgIEJPVExPR19DSEFUSUQsCiAgICAgICAgICAgICAgICAiI0NTUEFNXG4iCiAgICAgICAgICAgICAgICArIGYiTGV0dGVyIFNwYW0gd2FzIGV4ZWN1dGVkIHN1Y2Nlc3NmdWxseSBpbiBbVXNlcl0odGc6Ly91c2VyP2lkPXtldmVudC5jaGF0X2lkfSkgY2hhdCB3aXRoIDogYHttZXNzYWdlfWAiLAogICAgICAgICAgICApCiAgICAgICAgZWxzZToKICAgICAgICAgICAgYXdhaXQgZXZlbnQuY2xpZW50LnNlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgIEJPVExPR19DSEFUSUQsCiAgICAgICAgICAgICAgICAiI0NTUEFNXG4iCiAgICAgICAgICAgICAgICArIGYiTGV0dGVyIFNwYW0gd2FzIGV4ZWN1dGVkIHN1Y2Nlc3NmdWxseSBpbiB7ZXZlbnQuY2hhdC50aXRsZX0oYHtldmVudC5jaGF0X2lkfWApIGNoYXQgd2l0aCA6IGB7bWVzc2FnZX1gIiwKICAgICAgICAgICAgKQoKCkBib3Qub24oYWRtaW5fY21kKCJ3c3BhbSAoLiopIikpCkBib3Qub24oc3Vkb19jbWQocGF0dGVybj0id3NwYW0gKC4qKSIsIGFsbG93X3N1ZG89VHJ1ZSkpCmFzeW5jIGRlZiB0bWVtZShldmVudCk6CiAgICB3c3BhbSA9IHN0cigiIi5qb2luKGV2ZW50LnRleHQuc3BsaXQobWF4c3BsaXQ9MSlbMTpdKSkKICAgIG1lc3NhZ2UgPSB3c3BhbS5zcGxpdCgpCiAgICBhd2FpdCBldmVudC5kZWxldGUoKQogICAgZm9yIHdvcmQgaW4gbWVzc2FnZToKICAgICAgICBhd2FpdCBldmVudC5yZXNwb25kKHdvcmQpCiAgICBpZiBCT1RMT0c6CiAgICAgICAgaWYgZXZlbnQuaXNfcHJpdmF0ZToKICAgICAgICAgICAgYXdhaXQgZXZlbnQuY2xpZW50LnNlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgIEJPVExPR19DSEFUSUQsCiAgICAgICAgICAgICAgICAiI1dTUEFNXG4iCiAgICAgICAgICAgICAgICArIGYiV29yZCBTcGFtIHdhcyBleGVjdXRlZCBzdWNjZXNzZnVsbHkgaW4gW1VzZXJdKHRnOi8vdXNlcj9pZD17ZXZlbnQuY2hhdF9pZH0pIGNoYXQgd2l0aCA6IGB7bWVzc2FnZX1gIiwKICAgICAgICAgICAgKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIGF3YWl0IGV2ZW50LmNsaWVudC5zZW5kX21lc3NhZ2UoCiAgICAgICAgICAgICAgICBCT1RMT0dfQ0hBVElELAogICAgICAgICAgICAgICAgIiNXU1BBTVxuIgogICAgICAgICAgICAgICAgKyBmIldvcmQgU3BhbSB3YXMgZXhlY3V0ZWQgc3VjY2Vzc2Z1bGx5IGluIHtldmVudC5jaGF0LnRpdGxlfShge2V2ZW50LmNoYXRfaWR9YCkgY2hhdCB3aXRoIDogYHttZXNzYWdlfWAiLAogICAgICAgICAgICApCgoKQGJvdC5vbihhZG1pbl9jbWQoImRlbGF5c3BhbSAoLiopIikpCkBib3Qub24oc3Vkb19jbWQocGF0dGVybj0iZGVsYXlzcGFtICguKikiLCBhbGxvd19zdWRvPVRydWUpKQphc3luYyBkZWYgc3BhbW1lcihldmVudCk6CiAgICBpZiBldmVudC5md2RfZnJvbToKICAgICAgICByZXR1cm4KICAgIHJlcGx5ID0gYXdhaXQgZXZlbnQuZ2V0X3JlcGx5X21lc3NhZ2UoKQogICAgaW5wdXRfc3RyID0gIiIuam9pbihldmVudC50ZXh0LnNwbGl0KG1heHNwbGl0PTEpWzE6XSkuc3BsaXQoIiAiLCAyKQogICAgc2xlZXB0aW1ldCA9IHNsZWVwdGltZW0gPSBmbG9hdChpbnB1dF9zdHJbMF0pCiAgICBjYXQgPSBpbnB1dF9zdHJbMTpdCiAgICBhd2FpdCBldmVudC5kZWxldGUoKQogICAgYXdhaXQgc3BhbV9mdW5jdGlvbihldmVudCwgcmVwbHksIGNhdCwgc2xlZXB0aW1lbSwgc2xlZXB0aW1ldCwgRGVsYXlTcGFtPVRydWUpCgoKQ01EX0hFTFAudXBkYXRlKAogICAgewogICAgICAgICJzcGFtIjogIioqUGx1Z2luIDogKipgc3BhbWBcCiAgICAgICAgXG5cbioqICDigKIgIFN5bnRheCA6ICoqYC5zcGFtIDxjb3VudD4gPHRleHQ+YFwKICAgICAgICBcbioqICDigKIgIEZ1bmN0aW9uIDogKipfXyBGbG9vZHMgdGV4dCBpbiB0aGUgY2hhdCAhIV9fXAogICAgICAgIFxuXG4qKiAg4oCiICBTeW50YXggOiAqKmAuc3BhbSA8Y291bnQ+IHJlcGx5IHRvIG1lZGlhYFwKICAgICAgICBcbioqICDigKIgIEZ1bmN0aW9uIDogKipfX1NlbmRzIHRoZSByZXBsaWVkIG1lZGlhIDxjb3VudD4gdGltZXMgISFfX1wKICAgICAgICBcblxuKiogIOKAoiAgU3ludGF4IDogKipgLnNwc3BhbSByZXBseSB0byBzdGlja2VyYFwKICAgICAgICBcbioqICDigKIgIEZ1bmN0aW9uIDogKipfX3NwYW1zIHRoZSBjaGF0IHdpdGggYWxsIHN0aWNrZXJzIGluIHRoYXQgcGFja19fXAogICAgICAgIFxuXG4qKiAg4oCiICBTeW50YXggOiAqKmAuY3NwYW0gPHRleHQ+YFwKICAgICAgICBcbioqICDigKIgIEZ1bmN0aW9uIDogKipfXyBTcGFtIHRoZSB0ZXh0IGxldHRlciBieSBsZXR0ZXIuX19cCiAgICAgICAgXG5cbioqICDigKIgIFN5bnRheCA6ICoqYC53c3BhbSA8dGV4dD5gXAogICAgICAgIFxuKiogIOKAoiAgRnVuY3Rpb24gOiAqKl9fIFNwYW0gdGhlIHRleHQgd29yZCBieSB3b3JkLl9fXAogICAgICAgIFxuXG4qKiAg4oCiICBTeW50YXggOiAqKmAuZGVsYXlzcGFtIDxkZWxheT4gPGNvdW50PiA8dGV4dD5gXAogICAgICAgIFxuKiogIOKAoiAgRnVuY3Rpb24gOiAqKl9fIC5kZWxheXNwYW0gYnV0IHdpdGggY3VzdG9tIGRlbGF5Ll9fXAogICAgICAgIFxuXG5cbioqTm90ZSA6IFNwYW0gYXQgeW91ciBvd24gcmlzayAhISoqIgogICAgICAgICAgICB9CikK'))
