from .. import loader, utils


@loader.tds
class MAth(loader.Module):
    def calc(self, numo, do, numt):
        if do == ':':
            utils.answer(numo/numt)
        else:
            if do == '*':
                utils.answer(numo*numt)
            else:
                if do == '+':
                    utils.answer(numo+numt)
                else:
                    if do == '-':
                        utils.answer(numo-numt)
                    else:
                        if do == '%':
                            utils.answer(numo/100*numt)
                        else:
                            if do == '**':
                                utils.answer(numo**numt)

                


