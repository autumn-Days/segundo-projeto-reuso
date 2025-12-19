function mergesort(v) {
  if (v.length <= 1) return v;
  let m = Math.floor(v.length / 2);
  let l = mergesort(v.slice(0, m));
  let r = mergesort(v.slice(m));

  let res = [];
  while (l.length && r.length)
    res.push(l[0] < r[0] ? l.shift() : r.shift());

  return res.concat(l, r);
}

let v = mergesort([34,7,23,32,5,62,78,1,45,9,12,56,89,4,27,16,3,90,11,54,
                   21,8,67,14,29,6,10,2,99,41,18,25,30,15,55,19,28,13,20,17]);

console.log(v.join(" "));
