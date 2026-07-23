---
schema: qual/card@1
id: P-OX7OF
kind: problem
title: "8. Here we go:"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
8. Here we go:


  1. Let $\alpha(t) = e^{2\pi it}$ where $t \in [0, 1]$, be a loop in $S^1$ parameterized by $t$, which goes around $S^1$ exactly once. Then under the map $f: z \mapsto z^n$, we obtain $f(\alpha(t)) = e^{2\pi n i t}$ where $t \in [0,1]$. This resulting loop then goes around $S^1$ $n$ times, so the induced homomorphism on $\pi_1(S^1) = \ZZ$ is the map $f^*: \ZZ \into \ZZ$ given by $f^*(a) = na$.

  2. Define $\alpha$ as above, and define $f: S^1 \into S^1$ to be the antipodal map, so $f(z) = -z$ for $z \in S^1 \subset \CC$. We then left $\alpha$ to the fundamental group, and define $f_*([\alpha]) = [f \circ \alpha]$. Computing, we have $(f\circ \alpha)(t) = f(\alpha(t)) = -e^{2\pi i t}$. Where $\alpha(0) = \alpha(1) = 1 + 0i$, we have $(f\circ \alpha)(0) = (f\circ \alpha)(1) = -1 + 0i$. But note that $\alpha$ was a counter-clockwise loop in $S^1$, and the image of $\alpha$ is also a counter-clockwise loop. So this maps the generator $[\alpha] \in \pi_1(S^1, 1)$ to the generator $[\alpha'] \in \pi_1(S^1, -1)$. But since $S^1$ is path-connected, the fundamental groups at these two base points are isomorphic.
  Alternatively: the antipodal map on $S^1$ is homotopic to the identity map (since $n=1$ is odd), so $[f\circ \alpha] = [f][\alpha] = [\id][\alpha] = [\alpha]$, so the induced homomorphism on $\pi_1(S^1)$ is the identity map.

  3. Let $\alpha(t) = e^{it}$ where $t\in [0, 2\pi]$ be a counter-clockwise loop in $S^1$; then $[\alpha]$ generates the fundamental group. Then $f^*([\alpha]) = [(f\circ \alpha) (t)] = [e^{it} \mapsto e^{2\pi i \sin t}]$. Then just consider how $\sin$ behaves in each quadrant. In quadrant 1, as $t$ ranges from $0, \pi/2$ then $\sin t$ ranges from 0 to 1, so $\alpha$ is exactly traced out. In quadrant two, $\bar\alpha$ is traced out, since $\sin t$ decreases from 1 to 0. This happens again in the bottom quadrants, so we have $f^*([\alpha]) = [\alpha\bar\alpha\alpha\bar\alpha] = [\alpha][\alpha]^{-1}[\alpha][\alpha]^{-1} = [\id]$. But the identity element in $\ZZ$ is  0, so the induced homomorphism on $\ZZ$ is $f^*(a) = 0$, the homomorphism sending everything to 0.

