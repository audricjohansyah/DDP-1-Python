# Case 1 run program - should be no error
from PersianCat import PersianCat
from StrayCat import StrayCat
from Panda import Panda

persia_cat_afraid = PersianCat("Cat afraid", True)
persia_cat_brave = PersianCat("Cat brave", False)
stray_cat_naughty = StrayCat("Cat naughty", True)
stray_cat_not_naughty = StrayCat("Cat not naughthy", False)
stray_cat_not_naughty_not_aggressive = StrayCat("Cat not naughthy", False)
panda = Panda("panda")

persia_cat_afraid.play_with_hooman()
persia_cat_brave.play_with_hooman()
stray_cat_naughty.play_with_hooman()
stray_cat_not_naughty.play_with_hooman()
stray_cat_not_naughty_not_aggressive.is_aggressive = False
stray_cat_not_naughty_not_aggressive.play_with_hooman()
panda.sleep()

