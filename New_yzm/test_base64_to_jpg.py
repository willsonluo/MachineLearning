import base64
import yzm_predict_api

#code = base64.b64encode(open('yzm_download/1539575497643336.jpg','rb').read())
#yzm_predict_api.predict(code)
abc = base64.b64encode(open('yzm_download/1539575497643336.jpg','rb').read())
bcd = b'/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAWAEADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4 Tl5ufo6erx8vP09fb3 Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3 Pn6/9oADAMBAAIRAxEAPwD2ia4t4dMu7lZLYvao7SGafy40IXd 8bB2DBBJwcA5wafpypdWMV2ZI5Rcoko8mUSRKCo4jcBd6dSGIyc9hgDn/FyTHwR4mdlk8oaVeAM8oAGYRgKi8EZDcv8AMCCB8rU7wS0lj4D8NGK2T7GdMtAUgTMjSSBNzEcAKMlmPJOSeNvzAjU8Q3L6No15q8aRSQ2FrNcy27AhptiFgqvnCcjklW/Cq2havHqWi6fqF0ESS60uG NvFE5Ybl3PtOTvAyo2gZHGc7lrE IHizS7bwHrEF7ew6deXFjcRrYXZX7RJuWSJdqKxOC CGG5doJ4HIl8OQ3Frp2hwXUV0X0TTIYZrHyxuF3sESsnQsMeapcnyzkEH5WIALsXjHwzGsVm qRPqeyJfsUsqLdNI/yrGUyAJC3BXjaTzgc1L4i1yw8N6Gde1G7MFhE4k8kQESzK0ZCxBWOd5chugwBg4ALVxovPDEeia74bv4reS vtduGu9OmlMctw73amMIpZWLPE0RR1 TjLMoBNdT8QLO61TwXdLZ2Hn36RJdx2VzG8kUoililaJ1TKszbNoXOTkgHBY0AZX/CVeIbO50m91Pw2kWnarNbWgginmaWxd3Ks8u6BQAS8a4LdR8pYNkd5NDGsTMq4I965K38f6BO1pZ FQdburl0ItLJ8C3hCpudt FiVUKgKcZc7eG3EdBLKJLhI54990kcUjxJtZLYsJBvViFJzhk456fKoJNAyRz5iQoXlRY5A5Eb7d OQCcZxnBwCM4wcgkFjtcteC4E 3ZlUjwdhQlC24Z Z/kba3AG/oe5RQBLA/wBn80BpZFeQuBI 7ZnqoOM4zk4JOM4GAAA2dmncq2x7eRdksEqBlZcMCB05JK5zkYXGBkmiigCx9r/2P1qIzMlvIkHyyHcVaVmkAYknkE5IyemRxwMUUUAOM0ZmWYwKZVUqrn7wBwSAcdDtH5D0quIoVjWMRL5cbAwJtULAAu3CYAwMZ9/mI6cAooA//9k='
print(abc)
print(bcd)
print(abc == bcd)