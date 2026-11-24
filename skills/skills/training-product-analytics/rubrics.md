# Rubrics by question type

Used in the debrief. Each item is something a strong answer does,
roughly in order. Order matters less than coverage, except where marked
FIRST. Built from the sources in `cases.md`; the grouping is
`[my-synthesis]`.

## 1. Diagnose a metric change

- FIRST **Pin the metric.** Exact definition, what is divided by what,
  the time window, and what it is being compared with.
- FIRST **Is it real?** Tracking or definition change, late data, a
  normal seasonal swing, ordinary week-to-week noise.
- **Shape in time.** Sudden step or slow slide; one date or many.
- **Break the number into parts.** Volume, rate and mix: fewer people,
  a lower rate, or a shift toward groups with a lower rate.
- **Where.** Cut by platform, country, new versus existing, channel,
  plan. Look for one cut that holds most of the change.
- **What else moved.** Steps before and after it in the funnel.
- **Inside causes.** Releases, experiments, price or policy changes,
  marketing spend, by date.
- **Outside causes.** Season, competitors, other platforms, news.
- **Ranked guesses, each with its test.** Not a list of everything.
- **So what.** How big, whether to worry, what to do next.

Senior markers: says what would rule each guess out; notices when the
mix changed and no group's own rate did; sizes the loss in money.

Staff markers: asks whether this is the right number to be watching at
all; checks whether another team's change caused it or will be hit by
the fix; turns the investigation into a standing check so it need not
be done by hand again.

## 2. Define success measures

- FIRST **Goal and user.** What the feature is for, and for whom.
- **The moment of value.** The action that shows the user got it.
- **One main measure,** defined exactly: who counts, over what window.
- **A few supporting measures** that explain the main one.
- **Guardrails.** What must not get worse, including for other user
  groups and other products.
- **Early versus late.** A measure readable in days, tied to an outcome
  that takes months.
- **How it could be gamed** or rise for the wrong reason.
- **Proof the measure matters.** Show it predicts the long-run outcome.

Senior markers: resists a long list; separates "used it" from "better
off for it"; names who pays the cost if the measure is chased.

Staff markers: tests the measure against the company's top measure and
against other teams' targets; says what behaviour the measure will
create in the team that owns it; proposes how it is retired or revised.

## 3. Design an experiment

- FIRST **The claim,** stated so it could fail.
- **Who is in it.** Eligible users, and the point at which they count
  as exposed.
- **What is randomised.** User, page, account, region or time; chosen
  so one unit's treatment does not leak into another's.
- **Main measure and guardrails,** fixed before the start.
- **Size and length.** Smallest effect worth detecting, how many units
  that needs, and at least one full weekly cycle.
- **Health checks.** Planned split matches actual split; an identical
  versus identical run shows no difference.
- **Time effects.** Novelty wearing off, slow-building harm, a
  long-running holdout group.
- **Decision rule,** written in advance, including what happens on a
  mixed result.

Senior markers: spots interference between user groups; distrusts a
surprisingly large win; says what the test cannot tell you.

Staff markers: asks whether an experiment is the right tool or the
decision is already clear; weighs what the test costs in time and in
users exposed; sets a rule others can reuse for the same kind of test.

## 4. Measure impact with no experiment

- FIRST **What would have happened anyway.** Every method is a way of
  estimating that.
- **Threats to plain before-and-after.** Season, trend, other changes
  on the same date, a different mix of users afterwards.
- **A comparison group** not touched by the change, and why it is a
  fair one.
- **Method fitted to the situation.** Before-and-after with a
  comparison group; a modelled forecast from the period before; a
  cutoff rule that splits similar users; a staggered rollout.
- **Assumptions said out loud,** and a check on each where possible.
- **Range, not a point.** How far the answer moves under different
  reasonable choices.
- **Strength of evidence stated.** Weaker than an experiment, and by
  roughly how much.

Senior markers: looks for a natural comparison in how the change was
rolled out; refuses to give one number when two changes landed
together; proposes how to learn more next time.

Staff markers: says plainly when the question cannot be answered from
this data and what decision can still be made; changes how the next
launch is rolled out so it can be measured.

## 5. Trade-off or launch decision

- FIRST **Who gains, who loses.** Every user group and revenue line.
- **Common unit.** Put both sides in the same terms, usually money or
  long-run value per user.
- **Short term versus long term.** Which side grows with time.
- **Moved or created.** Is the gain new, or taken from elsewhere in
  the product.
- **Rough size** of each side, with the assumptions shown.
- **Can it be undone.** Cost of being wrong in each direction.
- **Recommendation with conditions,** and what to watch after.
- **What would change the call.**

Senior markers: finds a third option that keeps most of the gain;
separates what the data says from what the strategy wants; commits to
an answer.
Staff markers: names the strategic bet underneath the trade-off and who
owns that call; shows the effect on other product lines; says how the
decision will be reviewed and by when.

## Every type: edge cases and data considerations

Raised in round 3 of every case. Pick two from each list that bite on
the case in hand. Credit any the user raises unprompted.

**Data considerations**

- **How the number is recorded.** What event fires, when, and what is
  missed: blocked tracking, offline use, server versus device counts.
- **Definition drift.** The measure, or a filter inside it, changed
  partway through the period.
- **Late and missing data.** Recent days are incomplete; some records
  arrive days later or never.
- **Double counting.** One person with several accounts or devices;
  one action logged twice; retries.
- **Non-human activity.** Bots, internal staff, test accounts, the
  owner's own clicks.
- **Who is left out.** Only survivors are in the table; people who
  left early have no rows.
- **Joins that multiply or drop rows.** A total that changes after two
  tables are combined.
- **Time.** Time zones, week boundaries, holidays, daylight saving,
  month length.
- **Small groups.** A cut so fine that the result is noise.
- **Units.** Per user, per session or per account; currency; averages
  pulled by a few very large values.

**Edge cases**

- **A few heavy users dominate.** The top 1% produce most of the
  activity, so the average describes nobody.
- **The effect reverses by group.** Up overall, down in every group,
  or the other way round, because the mix shifted.
- **New versus existing users.** They react differently, and existing
  users react to change itself.
- **More than one user group.** A gain for one side is a cost to the
  other.
- **Moved, not made.** The gain was taken from another feature, plan
  or time period.
- **Timing.** A burst that fades, or a harm that builds slowly.
- **Free, trial and refunded states.** People who count as customers
  on one day and not the next.
- **Annual versus monthly commitments.** Some users cannot react for
  a year.
- **Countries and platforms.** Different prices, laws, payment methods
  and app versions.
- **The measure can be gamed,** by users or by the team that owns it.
- **Zero and empty cases.** Users with no activity, divisions by zero,
  accounts created and never used.
