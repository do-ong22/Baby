// 글 데이터를 담을 배열 (미리 샘플 글 넣기)
let posts = [
  { title: "첫 번째 글", content: "이건 샘플로 미리 작성된 글입니다 😊" },
  { title: "두 번째 글", content: "게시판 기능을 연습해보세요!" }
];

// 화면에 글 목록을 보여주는 함수
function renderPosts() {
  // 글 목록 초기화
  const postList = document.querySelector('#postList');
  postList.innerHTML = '';

  // 배열에 있는 글들을 카드 형태로 화면에 추가
  posts.forEach((post, index) => {
    postList.innerHTML += `
      <div class="card mb-2">
        <div class="card-body">
          <h5 class="card-title">${post.title}</h5>
          <p class="card-text">${post.content}</p>
          <button class="btn btn-danger btn-sm" data-index="${index}">삭제</button>
        </div>
      </div>
    `;
  });
}

// 글 작성 내용 가져오기
const form = document.querySelector('#postForm');

form.addEventListener('submit', (e) => {
  e.preventDefault(); // 새로고침 방지

  // 입력값 가져오기
  const title = document.querySelector('#title').value;
  const content = document.querySelector('#content').value;

  // 배열에 글 추가
  posts.push({ title, content });

  // 화면 갱신
  renderPosts();

  // 입력 초기화
  form.reset();
});

// 글 목록 삭제
const postList = document.querySelector('#postList');

postList.addEventListener('click', (e) => {
  if (e.target.tagName === 'BUTTON') {
    const index = e.target.dataset.index;
    posts.splice(index, 1); // 배열에서 글 제거
    renderPosts(); // 화면 갱신
  }
});

// 페이지 처음 열릴 때 미리 렌더링
renderPosts();
