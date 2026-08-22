---
schema: qual/card@1
id: E-SS1.EX-26
kind: exercise
title: "Suppose f is continuous in a region Ω"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
solved: false
---

::: exercise
26. Suppose f is continuous in a region Ω. Prove that any two primitives of f (if they exist) difer by a constant.

# 2 <sub>Cauchy’s</sub> <sub>Theorem</sub> <sub>and</sub> <sub>Its</sub> Applications

The solution of a large number of problems can be reduced, in the last analysis, to the evaluation of definite integrals; thus mathematicians have been much occupied with this task... However, among many results obtained, a number were initially discovered by the aid of a type of induction based on the passage from real to imaginary. Often passage of this kind led directly to remarkable results. Nevertheless this part of the theory, as has been observed by Laplace, is subject to various dificulties...

After having reflected on this subject and brought together various results mentioned above, I hope to establish the passage from the real to the imaginary based on a direct and rigorous analysis; my researches have thus led me to the method which is the object of this memoir...

A. L. Cauchy, 1827

In the previous chapter, we discussed several preliminary ideas in complex analysis: open sets in C, holomorphic functions, and integration along curves. The first remarkable result of the theory exhibits a deep connection between these notions. Loosely stated, Cauchy’s theorem says that if f is holomorphic in an open set Ω and $\gamma \subset \Omega$ is a closed curve whose interior is also contained in Ω then

$$

\int_ {\gamma} f (z) d z = 0.\tag{1}

$$

Many results that follow, and in particular the calculus of residues, are related in one way or another to this fact.

A precise and general formulation of Cauchy’s theorem requires defining unambiguously the “interior” of a curve, and this is not always an easy task. At this early stage of our study, we shall make use of the device of limiting ourselves to regions whose boundaries are curves that are “toy contours.” As the name suggests, these are closed curves whose visualization is so simple that the notion of their interior will be unambiguous, and the proof of Cauchy’s theorem in this setting will be quite direct. For many applications, it will sufice to restrict ourselves to these types of curves. At a later stage, we take up the questions related to more general curves, their interiors, and the extended form of Cauchy’s theorem.

Our initial version of Cauchy’s theorem begins with the observation that it sufices that f have a primitive in Ω, by Corollary 3.3 in Chapter 1. The existence of such a primitive for toy contours will follow from a theorem of Goursat (which is itself a simple special case)<sup>1</sup> that asserts that if f is holomorphic in an open set that contains a triangle T and its interior, then

$$

\int_ {T} f (z) d z = 0.

$$

It is noteworthy that this simple case of Cauchy’s theorem sufices to prove some of its more complicated versions. From there, we can prove the existence of primitives in the interior of some simple regions, and therefore prove Cauchy’s theorem in that setting. As a first application of this viewpoint, we evaluate several real integrals by using appropriate toy contours.

The above ideas also lead us to a central result of this chapter, the Cauchy integral formula; this states that if f is holomorphic in an open set containing a circle C and its interior, then for all z inside C,

$$

f (z) = \frac {1}{2 \pi i} \int_ {C} \frac {f (\zeta)}{\zeta - z} d \zeta .

$$

Diferentiation of this identity yields other integral formulas, and in particular we obtain the regularity of holomorphic functions. This is remarkable, since holomorphicity assumed only the existence of the first derivative, and yet we obtain as a consequence the existence of derivatives of all orders. (An analogous statement is decisively false in the case of real variables!)

The theory developed up to that point already has a number of noteworthy consequences:

<sub>•</sub> The property at the base of “analytic continuation,” namely that a holomorphic function is determined by its restriction to any open subset of its domain of definition. This is a consequence of the fact that holomorphic functions have power series expansions.
:::
