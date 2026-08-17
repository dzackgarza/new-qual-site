---
schema: qual/card@1
id: P-IMYQU
kind: problem
title: "2. Induct on $n$, integrate by parts and use L'Hopital:"
classification:
  areas:
  - prelim
  topics:
  - integrals
  - improper-integrals
  - integration-by-parts
  - induction
relations: []
review: draft
solved: false
---

::: problem
2. Induct on $n$, integrate by parts and use L'Hopital: Base case: $$n=1 \implies \int_0^\infty xe^{-x} = -xe^{-x}\bigg\rvert_0^\infty - \int_0^\infty -e^{-x} = \lim_{x\to\infty} \frac x {e^x}  + \lim_{x\to\infty} \frac 1 {e^x} + 1 \\ \equalsbecause{L.H.} \lim_{x\to\infty} \frac 1 {e^x}  + 0 + 1 = 1$$

   Inductive step:
   $$
   \int_0^\infty x^ne^{-x} = -x^ne^{-x}\bigg\rvert_0^\infty - \int_0^\infty -nx^{n-1}e^{-x} = -x^ne^{-x}\bigg\rvert_0^\infty + n \int_0^\infty x^{n-1}e^{-x} \\
   \equalsbecause{I.H.} -x^ne^{-x}\bigg\rvert_0^\infty + n (n-1)! \\
   \equalsbecause{L.H.$\times n$}0 + n(n-1)! = n!. \qed
   $$
:::
