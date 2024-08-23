import subprocess
import sys

def downgrade_numpy():
    # NumPy 2.0.0을 제거합니다.
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', 'numpy', '-y'])

    # 최신 1.x 버전의 NumPy를 설치합니다.
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy<2'])

# NumPy를 다운그레이드합니다.
downgrade_numpy()

# 성공 메시지를 출력합니다.
print("NumPy가 최신 1.x 버전으로 다운그레이드되었습니다. 코드를 다시 실행해보세요.")
