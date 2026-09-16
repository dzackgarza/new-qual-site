---
schema: qual/card@1
id: P-TRIV-PR13
kind: problem
title: 'Gambler''s ruin: absorption probabilities and mean duration of a random walk'
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 13, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains one or more nonprinting control bytes at this source position; they were removed from the authored card as nonsemantic extraction artifacts. The source includes Figure 8 illustrating the random walk; Flash preserves only the image placeholder/caption.
---

::: problem
”Random walk” Let A, B, x be integers, $A \leqslant x \leqslant B$ . Consider the particle that starts moving from the point x at time $t = 0$ . At each step $\Delta t = 1$ the particle can move left or right from its recent position with the probabilities p and $q = 1 - p$ correspondingly.
If at some step it reaches the points A or B, it stays there forever (see example figure below).

The source's Figure 8 illustrates one sample trajectory with $A=-B=5$ and $x=2$; the graphical trajectory is not present in the deterministic extraction.

(a) Assuming that the total number of steps approaches infinity, compute the probabilities $\alpha ( x ) , \beta ( x )$ to find the particle at the points A and B correspondingly, as functions of the initial position x of the particle.

(b) Find the mean time $m ( x )$ of a random walk of the particle before it hits A or B. Assume that $m ( x ) < \infty$ . Check that if $p = q = \frac { 1 } { 2 }$ and $A = - B$ , then $m ( 0 ) = B ^ { 2 }$ . Hence the mean time of random walk is given by a square of distance traveled.
:::
