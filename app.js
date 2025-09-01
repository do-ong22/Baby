// 글 데이터를 담을 배열
let posts = [];

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

const postList = document.querySelector('#postList');

postList.addEventListener('click', (e) => {
  if (e.target.tagName === 'BUTTON') {
    const index = e.target.dataset.index;
    posts.splice(index, 1); // 배열에서 글 제거
    renderPosts(); // 화면 갱신
  }
});