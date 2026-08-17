---
schema: qual/card@1
id: P-NESQN
kind: problem
title: "Let $A = S^n - \\theset{n_p = \\text{North Pole}}, B = S^n - \\theset{s_p = \\text{South Pole}}$. Then $A\\union B = S^n$ and $A\\intersect B = S^n - \\theset{n_p, s_p}$."
classification:
  areas:
  - topology
  topics:
  - fundamental-group
  - van-kampen
relations: []
review: draft
solved: false
---

::: problem
4. Let $A = S^n - \theset{n_p = \text{North Pole}}, B = S^n - \theset{s_p = \text{South Pole}}$.
   Then $A\union B = S^n$ and $A\intersect B = S^n - \theset{n_p, s_p}$.
   Since $A,B$ are open and path connected, we can apply van Kampen's theorem to obtain $\pi_1(X) = \pi_1(A) * \pi_1(B)$ amalgamated over $\pi_1(A\cap B)$.
   But $A \cong \RR^{n} \cong B$ via stereographic projection, and since $\RR^n$ is contractible, $\pi_1(\RR^n) = 0 = \pi_1(A) = \pi_1(B)$.
   So $\pi_1(X) = 0 * 0 = 0$ as desired.

This follow because we can compute $A \cap B \cong \RR^n - \theset{\text{pt}} \cong S^n{-1}$, and so $\pi_1(A\intersect B) = \pi_1(S^n) \cross \pi_1(\RR^1) = 0 \cross 0 = 0$, and so has the presentation $\pi_1(A\cap B) = \left< w \mid w^1 = e\right>$.
We can then look at the inclusions $i: A\cap B \into A$ $j: A\cap B \into B$ and the induced homomorphisms $I: \pi_1(A\cap B) \into \pi_1(A)$ $J: \pi_1(A\cap B) \into \pi_1(B)$.
But since both sides in both maps are trivial, these are constant maps between identities.
We can then present the group $0 = \pi_1(A) =\left< a\mid a^1 = e\right>$ and since $I(w) J(w)^{-1} = e e^{-1} = e$, we have $\pi_1(B) = \left< b \mid b^1 = e\right>$, so $\pi_1(A) *_{\pi_1(A\cap B)} \pi_1(B) = \left< a,b \mid a^1 =b^1 = e\right>$.

(See https://en.wikipedia.org/wiki/Seifert%E2%80%93van_Kampen_theorem for presentation of amalgamated product)
:::
