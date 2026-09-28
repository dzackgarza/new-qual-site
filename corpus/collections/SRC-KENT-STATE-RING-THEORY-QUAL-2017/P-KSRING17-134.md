---
schema: qual/card@1
id: P-KSRING17-134
kind: problem
title: Noetherian rings whose 2-generated ideals are principal
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 134 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked problem 134 on Ring_Theory_Qual_Problems.pdf PDF page 16 and added an erratum because the source omits the hypothesis that R is an integral domain.
---

::: {.problem}
[NEW] Let $R$ be a commutative Noetherian ring in which every 2-generated ideal is principal.
Prove that $R$ is a Principal Ideal Domain.
:::

::: {.remark}
Erratum: the statement is false as written in the source, which does not assume that $R$ is an integral domain.
The ring $R = \mathbb{Z}/4\mathbb{Z}$ is commutative and Noetherian, and every ideal of it is principal, but $2 \cdot 2 = 0$ with $2 \neq 0$, so $R$ is not a Principal Ideal Domain.
The intended statement adds the hypothesis that $R$ is an integral domain: then every ideal is finitely generated, and induction on the number of generators shows that every ideal is principal.
:::
