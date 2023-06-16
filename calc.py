from .. import loader, utils
@loader.tds
class MAth(loader.Module):
    def calc(self, numo, do, numt):
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

                
