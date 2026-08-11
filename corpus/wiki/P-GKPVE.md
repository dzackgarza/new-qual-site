---
schema: qual/card@1
id: P-GKPVE
kind: problem
title: "Since $f$ is irreducible of degree $n$ and $u$ is a root of $f$, the \u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

Since $f$ is irreducible of degree $n$ and $u$ is a root of $f$, the minimal polynomial of $u$ over $K$ is in fact $f$, and thus the degree of the extension $K(u) / K$ is given by

$$
[K(u) : K] = \deg \min(u, K) = n.
$$

To see that $K(u)$ is not Galois, we just note that since $f$ was irreducible, and $u$ was only one root of $f$, $K(u)$ is not the splitting field of $f$, and is thus not the splitting field of any other irreducible polynomial over $K$.

To see that $\mathrm{Aut}(K(u)/ K)$ is trivial, note that any $K\dash$automorphism of $K(u)$ can only send $u$ to one of its conjugates.
But the only conjugate of $u$ in $K(u)$ is $u$ itself, so only the identity automorphism can occur.
