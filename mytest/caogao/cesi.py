# function Base64(e) {
#     var _keyStr = "01234ABCDEFGHIJKLMNabcdefghijklmn+OPQRSTUVWXYZopqrstuvwxyz56789/=";
#
#     function encode(e) {
# for (var
#         t, r, o, n, a, i, s, u = "", c = 0; c < e.length;) n = (t = e[c++]) >> 2, a = (3 & t) << 4 | (r = e[c++]) >> 4, i = (15 & r) << 2 | (o = e[c++]) >> 6, s = 63 & o, u = isNaN(r) ? u + _keyStr.charAt(n) + _keyStr.charAt(a): isNaN(
#     o) ? u + _keyStr.charAt(n) + _keyStr.charAt(a) + _keyStr.charAt(i): u + _keyStr.charAt(n) + _keyStr.charAt(
#     a) + _keyStr.charAt(i) + _keyStr.charAt(s);


#         return u
#     }
#
#     return encode(e)
# }

# cars=["BMW","Volvo","Saab","Ford"];
# for (var i=0;i<cars.length;i++){
# 	document.write(cars[i] + "<br>");
# }


def Base64(e):
    _keyStr = "01234ABCDEFGHIJKLMNabcdefghijklmn+OPQRSTUVWXYZopqrstuvwxyz56789/="

    t, r, o, n, a, i, s, u = "", "", "", "", "", "", "", ""
    print(t, r, o, n, a, i, s, u)


if __name__ == '__main__':
    e = [
        165, 166, 112, 103, 102, 108, 106, 108, 100, 100, 105,
        110, 87, 166, 156, 157, 159, 112, 148, 107, 103, 107,
        148, 105, 103, 102, 103, 110, 97, 105, 151, 151, 106,
        152, 148, 153, 102, 100, 108, 155, 147, 151, 149, 109,
        99, 106, 107, 109, 101, 104, 89, 162, 150, 161, 112,
        103, 100, 99, 103, 92, 156, 169, 112, 102, 97, 99,
        99, 102, 149, 89, 148, 172, 110, 99, 100, 49, 51,
        51, 54
    ]
    Base64(e)
