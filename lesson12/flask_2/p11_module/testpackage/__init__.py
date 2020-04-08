# 导入模块后自动执行
print(f'导入了 {__name__} 包')

# import * 只导入mod1
__all__ = ['mod1']
# import * 导入定义过的模块
# __all__ = ['mod1', 'mod2']