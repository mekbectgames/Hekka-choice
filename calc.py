from .. import loader, utils
import requests


@loader.tds
class MAth(loader.Module):
    def math(self, numo, do, numt):
        "<Первое число> <Действие (+, -, :, *, %, **)> <Второе число>"
        if do == ':':
            await utils.answer(numo/numt)
        else:
            if do == '*':
                await utils.answer(numo*numt)
            else:
                if do == '+':
                    await utils.answer(numo+numt)
                else:
                    if do == '-':
                        await utils.answer(numo-numt)
                    else:
                        if do == '%':
                            await utils.answer(numo/100*numt)
                        else:
                            if do == '**':
                            await utils.answer(numo**numt)

                


