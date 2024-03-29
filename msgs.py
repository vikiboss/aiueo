from termcolor import colored as Color

msgs = {
    'a': '🎉 欢迎~ 这是练习假名的 Python 🎈 程序 - 《aiueo》\n🐈 Coded by Viki at 2020/12/5\n',
    'b': Color('😁 请先选择一个', 'cyan') + Color('练习模式', 'cyan', attrs=['bold', 'underline']),
    'c': Color('- 1.随机平假名模式\n- 2.随机片假名模式\n- 3.混合随机模式\n- 4.打乱复习模式\n- 5.查看假名表\n- 6.查看记忆口诀\n- 0.退出程序', 'blue'),
    'd': '>>> ',
    'e': Color('🎊 欢迎~ 开始%s练习叭~', 'cyan'),
    'f': Color('💡 tip: 输入 1 跳过当前题目, 输入 0 退出当前模式, 输入 kana 查看假名表', 'cyan'),
    'g': Color('%s ', 'blue', attrs=['bold']) + Color('怎么读: ', 'yellow'),
    'h': Color('✅', 'green'),
    'i': Color('❌ 答错了 再想想 (⊙x⊙;)', 'red'),
    'j': Color('%s', 'blue', attrs=['bold']) + Color(' 读作 ', 'cyan') + Color('%s', 'green', attrs=['bold']),
    'k': Color('💡 提示: %s', "cyan"),
    'l': Color(' 😅 下次记住~ 已跳过这题', 'cyan'),
    'm': Color('💨 已退出%s模式', 'cyan'),
    'n': Color('👋 拜拜ヾ(•ω•`)o 💓 我不在的时候也要好好学习哦', 'cyan'),
    'o': Color('📜 记忆口诀: %s', 'cyan'),
    'p': Color('⏰ 复习进度: %s/%s', 'cyan'),
    'q': Color('🎉 恭喜 你完成了今天的复习!', 'cyan'),
    'r': Color('⏰ 共花了 %s 秒 通过 %s/92 个 正确率 %s/%s 跳过 %s 个 错误假名有:\n%s', 'cyan'),
    's': Color('⏰ 进入乱序复习模式，计时开始！', 'cyan')
}
