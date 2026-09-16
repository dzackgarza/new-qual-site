---
schema: qual/card@1
id: PR-LF7SW
kind: proposition
title: Properties of Lebesgue outer measure
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $m_*$ be Lebesgue [[D-3XE77|outer measure]] on $\RR^n$ [@SS05, Chapter 1, Section 2].

(a) If $E\subseteq F\subseteq\RR^n$, then $m_*(E) \leq m_*(F)$.

(b) If $E_i\subseteq\RR^n$ for $i\geq1$, then $m_*\big(\bigcup_{i\geq1} E_{i}\big) \leq \sum_{i\geq1} m_*(E_{i})$.

(c) For every $E\subseteq\RR^n$ and $\varepsilon>0$ there exists an open set $G\supseteq E$ with $m_*(G) \leq m_*(E) + \varepsilon$.

(d) If $A,B\subseteq\RR^n$ satisfy $\dist(A,B)\coloneqq\inf\theset{\abs{a-b} : a\in A,\ b\in B}>0$, then $m_*(A\cup B) = m_*(A) + m_*(B)$.
:::

::: {.remark}
In (d), positive distance is sufficient but not necessary: for $A\coloneqq[0,1)$ and $B\coloneqq[1,2]$ in $\RR$, $\dist(A,B)=0$ and $m_*(A\cup B)=2=m_*(A)+m_*(B)$.
For disjoint sets in general, additivity fails: there are disjoint $A,B\subseteq\RR$ with $m_*(A\cup B)<m_*(A)+m_*(B)$, constructed from a non-measurable Vitali set.
:::
