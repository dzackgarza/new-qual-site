---
schema: qual/card@1
id: E-JY5OT
kind: exercise
title: "- Derive the reverse triangle inequality from the triangle inequality."
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
- Derive the reverse triangle inequality from the triangle inequality.
- Let $E\subseteq \RR$. Define $\sup E$ and $\inf E$.
- What is the **Archimedean** property?

### Metric Spaces / Topology
- What does it mean for a metric space to be **complete**?
- Give two or more equivalently definitions for **compactness** in a complete metric space.
- What is an interior point? An isolated point? A limit point?
- What does it mean for a set to be open? Closed?
- What is the **closure** of a subspace $E\subseteq X$?
- What does it mean for $E\subseteq X$ to be a **dense** subspace?
- What does it mean for a family of sets to form a **basis** for a topology?
	- What is a basis for the standard topology on $\RR^d$?
- Let $X$ be a subset of $\RR^d$. Prove the Heine-Borel theorem:
	- Show that $X$ compact $\implies X$ is closed
	- Show that $X$ compact $\implies X$ is bounded
	- Show that a closed subset of a compact set must be bounded.
	- Show that if $X$ closed and bounded $\implies X$ is compact. 
- Find an example of a metric space with a closed and bounded subspace that is not compact.
	- How can this be modified to obtain a necessary and sufficient condition?
- Determine if the following subsets of $\RR$ are opened, closed, both, or neither:
	- $\QQ$
	- $\ZZ$
	- $\ts{1}$
	- $\ts{p \in \ZZ^{\geq 0} \st p\text{ is prime}}$
	- $\ts{ {1\over n} \st n\in \ZZ^{\geq 0}}$
	-  $\ts{ {1\over n} \st n\in \ZZ^{\geq 0}} \union \ts{0}$

### Sequences
- Can a convergent sequence of real numbers have a subsequence converging to a different limit?
- What does it mean for a sequence of functions to converge **pointwise** and to converge **uniformly**?
	- Give an example of a sequence that converges pointwise but not uniformly.
- Prove that every sequence admits a monotone subsequence.
- Prove the monotone convergence theorem for sequences.
- Prove the Bolzano-Weierstrass Theorem.

### Series

-- What does it mean for a series to converge? How can you check this?
		- What does it mean for a series to converge *uniformly*? What do you have to show to prove it does *not* converge uniformly?
- Show that if $\sum_{n\in \NN} a_n < \infty$ converges, then $$a_n \ctz{n}$$.
- Show that convergent sequences *have small tails* in the following sense: $$\sum_{n > N} a_n \ctz{N}$$.
	- Is this a necessary and sufficient condition for convergence?
- State the ratio, root, integral, and alternating series tests.
- Prove that the harmonic series diverges
- Derive a formula for the sum of a geometric series.
- State and prove the $p\dash$test.
- What does it mean for a series to converge absolutely?
	- Find a sequence that converges but not absolutely.

### Continuity and Discontinuity

- What does it mean for a function to be **uniformly continuous** on a set?

- Is it possible for a function $f:\RR\to \RR$ to be discontinuous precisely on the rationals $\QQ$? If so, produce such a function, if not, why?
	- Can the set of discontinuities be precisely the irrationals $\RR\sm\QQ$?

- Find a sequence of continuous functions that does *not* converge uniformly, but still has a pointwise limit that is continuous.

